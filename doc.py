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
   
def opens(x):
    df = pd.read_csv(x)
    return ''.join(str(e) for e in df['0'])

def nlpx(lst,symbol):
    nlp = spacy.load("zh_core_web_sm")
    for r in range(len(lst)-1):
        doc1 = nlp(lst[r])
        doc2 = nlp(lst[r+1])
        n.append(doc1.similarity(doc2))
        sym.append(symbol)
        # 存成2維或dict

dt = pd.read_csv("lst1.csv")
#懷疑這裡
for symbol in dt['0']:
    for i in range(2011,2020):
        try:
            path = "zip/"+str(i)+'/'+str(symbol)+".csv"
            # 補上缺失
        except FileNotFoundError:
            pass
            
        lst.append(opens(path))
        nlpx(lst,symbol)
        
        break
        
dic = [[symbol],[lst]]
        




