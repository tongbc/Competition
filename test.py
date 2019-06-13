# coding=gbk
import numpy as np
import torch
import torch.nn as nn
import gensim
# model = gensim.models.KeyedVectors.load_word2vec_format('./word2vec/word2vec_wx')
model = gensim.models.Word2Vec.load('./word2vec/word2vec_wx')
print(model[u"操蛋"])
# word_2x = np.load("./word2vec/word2vec_wx.wv.syn0.npy")
# weights = torch.FloatTensor(word_2x)
# embedding = nn.Embedding.from_pretrained(weights)
# input = torch.LongTensor([3])
# print(embedding(input))
