# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 02:17:06 2015

@author: nausheenfatma
"""
import gensim,logging
def mysen():
    i=0
    for line in open("sample_corpus.txt","r"):
        print "train",i+1
        i=i+1
        yield line.split()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)
sentences=mysen()
model=gensim.models.Word2Vec(sentences,min_count=1,size=50) #dimension=50
model.save('sample_corpus.model')
model.save_word2vec_format('sample_corpus.model.bin', binary=True)

f=open("sample_corpus_vocab.txt","r")
j=0
f2=open("embeddings.txt","w")
for line in f:
    print j+1
    j=j+1
    word=line.rstrip()
    a=(model[word])
    #print a
    #additional code below to write without commas and brackets
    s=""
    for e in a:
        s=s+str(e)+" "
    s=s.rstrip(" ")
    #print word
    #print model[word]
    f2.write(str(s)+"\n")
f2.close() 
#print model["बिहार"]
