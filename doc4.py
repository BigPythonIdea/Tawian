# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:44:06 2021

@author: Mooncat
ind = []
for d in dirs:
    ind.append(PATH+"\\"+d)

row = []
for i in ind:
    ind_path = os.listdir(i)
    for r in ind_path:
        dfx = pd.read_csv(i+"\\"+r)
        r = int(str(r).replace(".csv", ""))
        content = str(dfx["Year"])
        print(content)
        break
"""

import pandas as pd
import os

PATH = 'C:\\Users\Mooncat\py\TawianLab\Industry'
dirs = os.listdir(PATH)

df = pd.read_csv("Taiwans.csv")
a = df["Content"][108]
b = df["Content"][129]

Y_16 = []
Y_17 = []
Y_18 = []
Y_19 = []
Y_20 = []

dfx = pd.read_csv(PATH+"\\化學\\1708.csv")






    

    
        