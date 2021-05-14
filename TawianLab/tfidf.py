# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:14:09 2021

@author: Mooncat
"""
import math
import pandas as pd

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