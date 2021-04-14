# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:26:45 2021

@author: Solana
"""

import pandas as pd
import spacy




lst = []
n = []
sym = []
lsdx = []


dx = pd.read_csv("lst1.csv")
for x in dx["0"]:
    lsdx.append(x)
    
def opens(x):
    try:
        df = pd.read_csv(x)
        return ''.join(str(e) for e in df['0'])
    except:
        return ''

def nlpx(lst,symbol):
    nlp = spacy.load("zh_core_web_sm")
    for r in range(len(lst)-1):
        try:
            doc1 = nlp(lst[r])
            doc2 = nlp(lst[r+1])
            n.append(doc1.similarity(doc2))
            sym.append(symbol)
        except:
            n.append(" ")

for symbol in lsdx:
    for i in range(2011,2020):
        path = "zip/"+str(i)+'/'+str(symbol)+".csv"
        lst.append(opens(path))
        nlpx(lst,symbol)
    
