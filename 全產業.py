# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:28:01 2021

@author: Mooncat
df["Year"]
df["Symbol"]
df["score"]
"""

import pandas as pd
from glob import glob

INDUSTRYS = ["化學","水泥","半導體","生技","光電","百貨","光電","汽車","其他","其他電子"
             ,"油電燃氣","金融","玻璃","紡織","通訊網路","造紙","塑膠","資訊服務","運輸"
             ,"電子通路","電子零件","電腦周邊","電器","電機","橡膠","鋼鐵","營造","觀光"]


path = "C:\\Users\\Mooncat\\py\\TawianLab"
files =  glob(path+"/*.csv")

df = pd.concat(
    (pd.read_csv(file, usecols=['Year','Symbol','score'], 
                 dtype={ 'Year': str, 'Symbol':str, 'score':str}) for file in files), ignore_index=True)
        
    
df.to_csv("全產業比較.csv")



    
    