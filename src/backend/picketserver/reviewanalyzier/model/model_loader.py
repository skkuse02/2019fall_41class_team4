import numpy as np
from mxnet.gluon import nn, rnn
from mxnet import gluon, autograd
import gluonnlp as nlp
import mxnet as mx

from kobert.mxnet_kobert import get_mxnet_kobert_model
from kobert.utils import get_tokenizer
from keras.callbacks import ModelCheckpoint


class BERTDataset(mx.gluon.data.Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer, max_len, pad, pair):
        transform = nlp.data.BERTSentenceTransform(bert_tokenizer, max_seq_length=max_len, pad=pad, pair=pair)
        sent_dataset = gluon.data.SimpleDataset([[i[sent_idx], ] for i in dataset])
        self.sentences = sent_dataset.transform(transform)
        self.labels = gluon.data.SimpleDataset(
            [np.array(np.int32(i[label_idx])) for i in dataset])

    def __getitem__(self, i):
        return self.sentences[i] + (self.labels[i], )

    def __len__(self):
        return len(self.labels)


class BERTClassifier(nn.Block):
    def __init__(self, bert, prefix=None, params=None):
        super(BERTClassifier, self).__init__(prefix=prefix, params=params)
        self.bert = bert

        with self.name_scope():
            self.classifier = gluon.nn.SymbolBlock.imports("lenet-symbol.json", ['data'], "lenet-0001.params", ctx=ctx)

    def forward(self, inputs, token_types, valid_length=None):
        _, pooler = self.bert(inputs, token_types, valid_length)
        return self.classifier(pooler)


ctx = mx.gpu() if mx.context.num_gpus() else mx.cpu()

bert_base, vocab = get_mxnet_kobert_model(use_decoder=False, use_classifier=False, ctx=ctx)
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

dataset_test = nlp.data.TSVDataset("ratings_test.txt", field_indices=[1, 2], num_discard_samples=1)

max_len = 128
data_test = BERTDataset(dataset_test, 0, 1, tok, max_len, True, False)
model = BERTClassifier(bert_base)

model.hybridize()
batch_size = 32
test_dataloader = mx.gluon.data.DataLoader(data_test, batch_size=int(batch_size))

for batch_id, (token_ids, valid_length, segment_ids) in enumerate(test_dataloader):
    with mx.autograd.record():
        # load data to GPU
        token_ids = token_ids.as_in_context(ctx)
        valid_length = valid_length.as_in_context(ctx)
        segment_ids = segment_ids.as_in_context(ctx)

        # forward computation
        out = model(token_ids, segment_ids, valid_length.astype('float32'))


