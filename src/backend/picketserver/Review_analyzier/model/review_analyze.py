import numpy as np
from mxnet.gluon import nn, rnn
from mxnet import gluon, autograd
import gluonnlp as nlp
import mxnet as mx

from kobert.mxnet_kobert import get_mxnet_kobert_model
from kobert.utils import get_tokenizer


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
    def __init__(self, bert, num_classes=2, dropout=None, prefix=None, params=None):
        super(BERTClassifier, self).__init__(prefix=prefix, params=params)
        self.bert = bert

        with self.name_scope():
            self.classifier = nn.HybridSequential(prefix=prefix)
            if dropout:
                self.classifier.add(nn.Dropout(rate=dropout))
            self.classifier.add(nn.Dense(units=num_classes))

    def forward(self, inputs, token_types, valid_length=None):
        _, pooler = self.bert(inputs, token_types, valid_length)
        return self.classifier(pooler)


ctx = mx.cpu()

bert_base, vocab = get_mxnet_kobert_model(use_decoder=False, use_classifier=False, ctx=ctx)

tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

dataset_train = nlp.data.TSVDataset("ratings_train.txt", field_indices=[1, 2], num_discard_samples=1)
dataset_test = nlp.data.TSVDataset("ratings_test.txt", field_indices=[1, 2], num_discard_samples=1)

max_len = 128
data_train = BERTDataset(dataset_train, 0, 1, tok, max_len, True, False)
data_test = BERTDataset(dataset_test, 0, 1, tok, max_len, True, False)

model = BERTClassifier(bert_base, num_classes=2, dropout=0.1)

model.classifier.initialize(init=mx.init.Normal(0.02), ctx=ctx)
model.hybridize()

# softmax cross entropy loss for classification
loss_function = gluon.loss.SoftmaxCELoss()

