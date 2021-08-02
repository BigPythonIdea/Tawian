# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:56:05 2021

@author: Mooncat
"""

import pandas as pd


df = pd.read_csv("Taiwans.csv")
a = df["Content"][108]
b = df["Content"][129]

key = [1101,1102,1103,1104,1108,1109,1110]
point = []
other = []

for i in key:
    ga = df[(df.Symbol == i) & (df.Content == a)].index.tolist()
    point.append(ga)
    gb = df[(df.Symbol == i) & (df.Content == b)].index.tolist()
    other.append(gb)


def article(star,end,k):
    lst = []
    for i in range(star,end):
        lst.append(df["Content"][i])
    dt = pd.DataFrame(lst)
    dt.to_csv(str(k)+".csv", encoding="utf_8_sig")
        



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
for i in range(length-1):
    lst.append(p.pop(0))
    lst.append(o.pop(0))
print(lst)

for k in key:
    for i in range(len(lst)):
        try:
            article(lst[i], lst[i+1],k)
        except IndexError:
            break
