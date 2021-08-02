# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:44:06 2021

@author: Mooncat

1. a b = 1
2. not b
"""

import pandas as pd
import os


INDUSTRY = '化學'
PATH = 'C:\\Users\Mooncat\py\TawianLab\Industry'+'\\'+INDUSTRY
dirs = os.listdir(PATH)

key = []
for dirs_ in dirs:
    key.append(int(dirs_[0:4]))

df = pd.read_csv("T16.csv")
a = df["Content"][108]
b = df["Content"][129]


point = []
other = []


for i in key:
    ga = df[(df.Symbol == i) & (df.Content == a)].index.tolist()
    point.append(ga)
    gb = df[(df.Symbol == i) & (df.Content == b)].index.tolist()
    if not gb:
        print(i)
    other.append(gb)


def article(star,end,k):
    lst = []
    for i in range(star,end):
        lst.append(df["Content"][i])
    dt = pd.DataFrame(lst)
    # dt.to_csv(str(k)+".csv", encoding="utf_8_sig")
        



p = []
for s in point:
    for r in s:
        p.append(r)
    
o = []
for s in other:
    for r in s:
        o.append(r)

lst = []
length = len(p)+1

try:
    for i in range(length-1):
        lst.append(p.pop(0))
        lst.append(o.pop(0))
    print(lst)
except IndexError:
    print("IndexError")


for k in key:
    for i in range(len(lst)):
        try:
            article(lst[i], lst[i+1],k)
        except IndexError:
            break
    


        
        







    

    
        
