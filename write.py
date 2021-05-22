# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:37:41 2021

@author: Mooncat
"""

import pandas as pd

def write_txt(sym,year):
    path = "C:\\Users\\Mooncat\\py\\Tawian\\zip\\"
    store_dir = "C:\\Users\\Mooncat\\py\\TawianLab\\zip\\"+year+"\\"
    d1 = pd.read_csv(path+year+"\\"+str(sym)+".csv")
    outstr = ''
    for i in d1['0']:
        if i != " " and i != "\n":
            outstr += i
    
    with open(store_dir+str(sym)+".txt", 'w+', encoding="utf-8")as f:
        f.write(outstr)
    
    return str(sym)