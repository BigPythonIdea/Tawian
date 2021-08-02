# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 21:35:05 2021

@author: Mooncat
"""

import pandas as pd
import os

INDUSTRYS = ["電腦周邊"]
PATH = "C:\\Users\\Mooncat\\py\\TawianLab\\ok\\"
Year = []
key = []
key2 = []

for INDUSTRY in INDUSTRYS:
    for YEAR in range(2011,2021):
        with open(PATH+INDUSTRY+"\\"+INDUSTRY+".csv"+str(YEAR)+".txt", "r" )as f:
            for fs in f:
                st = fs.split(':')
                Year.append(YEAR)
                key.append(st[0])
                key2.append(st[1])
    

dic = pd.DataFrame({
          "Year":Year,
          "Symbol":key,
          "score":key2
      })

dic.to_csv(str(INDUSTRYS[0])+".csv",index=False)



                


