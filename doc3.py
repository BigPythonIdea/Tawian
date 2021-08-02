# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:55:04 2021

@author: Mooncat
"""

import pandas as pd
import os

PATH = 'C:\\Users\Mooncat\py\TawianLab\symbol'
PATH_A = 'C:\\Users\Mooncat\py\TawianLab'


df = pd.read_csv("Taiwans.csv")



for dirname in os.walk(PATH):
    for INDUSTRY in dirname[2]:
        try:
            os.mkdir(str(INDUSTRY).replace(".csv",""))
        except:
            pass
        dfs = pd.read_csv(PATH+"\\"+INDUSTRY)
        lst = list(dfs["代碼"])
        for i in lst:
            ga = df[df.Symbol == i]
            ga.to_csv(PATH_A+"\\"+str(INDUSTRY).replace(".csv","")+"\\"+str(i)+".csv", encoding="utf_8_sig")

        
        
          