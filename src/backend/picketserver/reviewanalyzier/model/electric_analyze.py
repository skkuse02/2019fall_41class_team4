import numpy as np
from mxnet.gluon import nn, rnn
from mxnet import gluon, autograd
import gluonnlp as nlp
import mxnet as mx

from kobert.mxnet_kobert import get_mxnet_kobert_model
from kobert.utils import get_tokenizer
from .Bertdata import BERTDataset


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


ctx = mx.gpu() if mx.context.num_gpus() else mx.cpu()


def evaluate_accuracy(model, data_iter, ctx=ctx):
    acc = mx.metric.Accuracy()
    i = 0
    for i, (t,v,s, label) in enumerate(data_iter):
        token_ids = t.as_in_context(ctx)
        valid_length = v.as_in_context(ctx)
        segment_ids = s.as_in_context(ctx)
        label = label.as_in_context(ctx)
        output = model(token_ids, segment_ids, valid_length.astype('float32'))
        acc.update(preds=output, labels=label)
        if i > 1000:
            break
        i += 1
    return acc.get()[1]


bert_base, vocab = get_mxnet_kobert_model(use_decoder=False, use_classifier=False, ctx=ctx)

tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

dataset_train = nlp.data.TSVDataset("electric_dataset.txt", field_indices=[1, 2], num_discard_samples=1)

max_len = 128
data_train = BERTDataset(dataset_train, 0, 1, tok, max_len, True, False)

model = BERTClassifier(bert_base, num_classes=2, dropout=0.1)

model.classifier.initialize(init=mx.init.Normal(0.02), ctx=ctx)
model.hybridize()

# softmax cross entropy loss for classification
loss_function = gluon.loss.SoftmaxCELoss()

batch_size = 32
lr = 5e-5

train_dataloader = mx.gluon.data.DataLoader(data_train, batch_size=batch_size)

trainer = gluon.Trainer(model.collect_params(), 'bertadam', {'learning_rate': lr, 'epsilon': 1e-9, 'wd':0.01})
log_interval = 4
num_epochs = 5

# LayerNorm과 Bias에는 Weight Decay를 적용하지 않는다.
for _, v in model.collect_params('.*beta|.*gamma|.*bias').items():
    v.wd_mult = 0.0
params = [
    p for p in model.collect_params().values() if p.grad_req != 'null'
]

# learning rate warmup을 위한 준비
accumulate = 4
step_size = batch_size * accumulate if accumulate else batch_size
num_train_examples = len(data_train)
num_train_steps = int(num_train_examples / step_size * num_epochs)
warmup_ratio = 0.1
num_warmup_steps = int(num_train_steps * warmup_ratio)
step_num = 0
all_model_params = model.collect_params()

# Set grad_req if gradient accumulation is required
if accumulate and accumulate > 1:
    for p in params:
        p.grad_req = 'add'

for epoch_id in range(num_epochs):
    metric.reset()
    step_loss = 0
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(train_dataloader):
        if step_num < num_warmup_steps:
            new_lr = lr * step_num / num_warmup_steps
        else:
            non_warmup_steps = step_num - num_warmup_steps
            offset = non_warmup_steps / (num_train_steps - num_warmup_steps)
            new_lr = lr - offset * lr
        trainer.set_learning_rate(new_lr)
        with mx.autograd.record():
            # load data to GPU
            token_ids = token_ids.as_in_context(ctx)
            valid_length = valid_length.as_in_context(ctx)
            segment_ids = segment_ids.as_in_context(ctx)
            label = label.as_in_context(ctx)

            # forward computation
            out = model(token_ids, segment_ids, valid_length.astype('float32'))
            ls = loss_function(out, label).mean()

        # backward computation
        ls.backward()
        if not accumulate or (batch_id + 1) % accumulate == 0:
            trainer.allreduce_grads()
            nlp.utils.clip_grad_global_norm(params, 1)
            trainer.update(accumulate if accumulate else 1)
            step_num += 1
            if accumulate and accumulate > 1:
                # set grad to zero for gradient accumulation
                all_model_params.zero_grad()

        step_loss += ls.asscalar()
        metric.update([label], [out])
        if (batch_id + 1) % 50 == 0:
            print('[Epoch {} Batch {}/{}] loss={:.4f}, lr={:.10f}, acc={:.3f}'
                         .format(epoch_id + 1, batch_id + 1, len(train_dataloader),
                                 step_loss / log_interval,
                                 trainer.learning_rate, metric.get()[1]))
            step_loss = 0

        model.classifier.export('electric.ckp', epoch=epoch_id)
