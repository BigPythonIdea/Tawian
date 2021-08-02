# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:22:31 2021

@author: Mooncat
"""

import pandas as pd

Year = []
key = []
key2 = []

with open('KeyAuditMatter_Taiwans.txt', 'r', encoding='utf-8') as f:
    for w in f:
        key.append(w[0:4])
        Year.append(w[23:30])
        key2.append(w[42:])

dic = pd.DataFrame({
          "Symbol":key,
          "Year":Year,
          "Content":key2
      })

C_16 = []
C_17 =[] 
C_18 = []
C_19 = []
C_20 = []

S_16 = []
S_17 =[] 
S_18 = []
S_19 = []
S_20 = []

for i in range(len(dic)):
    if dic.Year[i][0:4] == "2016":
        C_16.append(dic.Content[i])
        S_16.append(dic.Symbol[i])
    if dic.Year[i][0:4] == "2017":
        C_17.append(dic.Content[i])
        S_17.append(dic.Symbol[i])
    if dic.Year[i][0:4] == "2018":
        C_18.append(dic.Content[i])
        S_18.append(dic.Symbol[i])
    if dic.Year[i][0:4] == "2019":
        C_19.append(dic.Content[i])
        S_19.append(dic.Symbol[i])
    if dic.Year[i][0:4] == "2020":
        C_20.append(dic.Content[i])
        S_20.append(dic.Symbol[i])

dic16 = pd.DataFrame({
          "Symbol":S_16,
          "Content":C_16
      })

dic17 = pd.DataFrame({
          "Symbol":S_17,
          "Content":C_17
      })  

dic18 = pd.DataFrame({
          "Symbol":S_18,
          "Content":C_18
      })

dic19 = pd.DataFrame({
          "Symbol":S_19,
          "Content":C_19
      })

dic20 = pd.DataFrame({
          "Symbol":S_20,
          "Content":C_20
      })   
  
dic16.to_csv("T16.csv",index=False, encoding='utf_8_sig')
dic17.to_csv("T17.csv",index=False, encoding='utf_8_sig')
dic18.to_csv("T18.csv",index=False, encoding='utf_8_sig')
dic19.to_csv("T19.csv",index=False, encoding='utf_8_sig')
dic20.to_csv("T20.csv",index=False, encoding='utf_8_sig')