# -*- coding: utf-8 -*-
"""
Created on Sat May  8 14:49:18 2021

@author: Mooncat
"""

import pandas as pd
import numpy as np
import jieba
import os
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity
from lab import get_one_row_text


sym = get_one_row_text(1101)
sym1 = get_one_row_text(1102)



s1 = ""
with open(sym+".txt", 'r', encoding="utf-8") as f:
    for line in f.readlines():
        s1 += line
        

s2 = ""
with open(sym1+".txt", 'r', encoding="utf-8") as f1:
    for line in f1.readlines():
        s2 += line
        

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def jieba_(lst,v=None):
    jieba.set_dictionary("dict.txt")
    jie = jieba.cut(lst)
    stop = stopwordslist("stop.txt")
    outstr = ''
    for word in jie:
        if word not in stop:
            if word != '\n' and word!=" ":
                outstr += word
    return outstr


j1 = jieba_(s1)
j2 = jieba_(s2)


def tf_idf(str1,str2,v=None):
    # corpus = [str1,str2]
    # vectorizer = TfidfVectorizer()
    # X = vectorizer.fit_transform(corpus)
    # print(X[0])
    doc_all = [str1,str2]
    doc_all = [[word.lower() for word in doc.split() if len(word) >= 2] for doc in doc_all]
    
    #tf
    tf = dict()
    for n in range(len(doc_all)):
        for word in doc_all[n]:
            if word not in tf: 
                tf[word] = [0 for _ in doc_all]
            tf[word][n] = sum([1 for term in doc_all[n] if term == word])/len(doc_all[n])
    
    #IDF
    total_D = len(doc_all)
    idf = dict()
    for doc in doc_all:
        for word in doc:
            if word not in idf:
                word_idf = math.log(total_D/sum([1 for doc in doc_all if word in doc])+1)
                idf[word] = word_idf
    
    # TF-IDF
    sorted_word = sorted(set([word for word in tf]))
    tfidf = list()
    for word in sorted_word:
        value = tf[word]
        value = [v*idf[word] for v in value]
        tfidf.append(value)

    return pd.DataFrame(tfidf)


vector = tf_idf(j1,j2)
