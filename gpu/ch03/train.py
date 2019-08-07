import sys
import cupy as cp
sys.path.append('..')
from ch01.trainer import Trainer
from ch01.optimizer import Adam
from simple_cbow import SimpleCBOW
from util import preprocess, create_contexts_target, convert_one_hot

#import ipdb; ipdb.set_trace()

window_size = 1
hidden_size = 5
batch_size = 3
max_epoch = 1000

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)

vocab_size = len(word_to_id)
contexts, target = create_contexts_target(corpus, window_size)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

model = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()