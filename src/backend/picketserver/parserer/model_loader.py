import numpy as np
from mxnet.gluon import nn, rnn
from mxnet import gluon, autograd
import gluonnlp as nlp
import mxnet as mx

from .kobert.mxnet_kobert import get_mxnet_kobert_model
from .kobert.utils import get_tokenizer

from .BERTdata import BERTDataset


def run_model(review_list):
	ctx = mx.gpu() if mx.context.num_gpus() else mx.cpu()
	
	print(review_list)
	class BERTClassifier(nn.Block):
		def __init__(self, bert, num_classes=2, dropout=None, prefix=None, params=None):
		    super(BERTClassifier, self).__init__(prefix=prefix, params=params)
		    self.bert = bert

		    with self.name_scope():
		        self.classifier = nn.SymbolBlock.imports("electric.ckp-symbol.json", ['data'], "electric.ckp-0009.params", ctx=ctx)

		def forward(self, inputs, token_types, valid_length=None):
		    _, pooler = self.bert(inputs, token_types, valid_length)
		    return self.classifier(pooler)
  
	bert_base, vocab = get_mxnet_kobert_model(use_decoder=False, use_classifier=False, ctx=ctx)
	tokenizer = get_tokenizer()
	tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)
	print("b")
	ifptr = open("temp_file.txt", 'w', encoding='cp949')
	for review in review_list:
		review_parse = review.split(' ')
		
		sentence_length = 0
		new_sentence = ""
		
		for i in range(len(review_parse) - 1, max(-1, len(sentence_parse) - 8), -1):
			new_sentence = review_parse[i] + " " + new_sentence
			sentence_length += len(review_parse[i])
			
			if sentence_length >= 30:
				break
		
		new_sentence = new_sentence[:-1]
		
		data = str(0) + "\t" + new_sentence + "\t" + str(0) + "\n"
		ifptr.write(data);
	print("WTF")
	ifptr.close()
	
	dataset_test = nlp.data.TSVDataset("temp_file.txt", field_indices=[1, 2], num_discard_samples=1)

	max_len = 128
	data_test = BERTDataset(dataset_test, 0, 1, tok, max_len, True, False)
	model = BERTClassifier(bert_base)

	model.hybridize()
	batch_size = 50
	test_dataloader = mx.gluon.data.DataLoader(data_test, batch_size=int(batch_size))
	
	prediction = np.zeros(len(review_list))
	for batch_id, (token_ids, valid_length, segment_ids) in enumerate(test_dataloader):
	    with mx.autograd.record():
		# load data to GPU
                token_ids = token_ids.as_in_context(ctx)
                valid_length = valid_length.as_in_context(ctx)
                segment_ids = segment_ids.as_in_context(ctx)

		# forward computation
                out = model(token_ids, segment_ids, valid_length.astype('float32'))
                output = np.argmax(out, axis=1)
                prediction[batch_id*batch_size:min((batch_id+1)*batch_size, len(review_list))]
	
	return prediction


