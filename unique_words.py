# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:13:57 2015

@author: nausheenfatma
"""

#To make vocabulary file

f1=open("sample_corpus.txt","r")
f2=open("sample_corpus_vocab.txt","w")
unique_words=[]
i=0
for word in f1.readline().split():
    i=i+1
    #print i
    if not word in unique_words:
        unique_words.append(word)
        f2.write(word+'\n')
f2.close()
    
