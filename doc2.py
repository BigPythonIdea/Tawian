# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 14:38:49 2021

@author: Mooncat
"""

import pandas as pd

df = pd.read_csv("Taiwans.csv")
key = [1101,1102,1103,1104,1108,1109,1110]
a = df["Content"][108]
b = df["Content"][129]
point = []
other = []

def merger(lst,v=None):
    if v is None:
        op = []
    for i in lst:
        for r in i:
            op.append(r)
    return op

def article(star,end,k):
    lst = []
    for i in range(star,end):
        lst.append(df["Content"][i])
    dt = pd.DataFrame(lst)
    dt.to_csv(str(k)+".csv", encoding="utf_8_sig")


try:
    for i in key:
        ga = df[(df.Symbol == i) & (df.Content == a)].index.tolist()
        point.append(ga)
        gb = df[(df.Symbol == i) & (df.Content == b)].index.tolist()
        other.append(gb)
    point = merger(point)
    other = merger(other)
except:
    print(i)
    