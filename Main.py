# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:37:27 2021

@author: Mooncat
"""

import pandas as pd
import os
import numpy as np
import time
from sklearn.metrics.pairwise import cosine_similarity
from write import write_txt
from jiebas import jieba_
from tfidf import tf_idf

INDUSTRY = "化學.csv"
YEAR = "2012"
PATH = "C:\\Users\\Mooncat\\py\\Tawian\\zip\\"
PATH_SYMBOL = "C:\\Users\\Mooncat\\py\\Tawian\\symbol\\"
store_dir = "C:\\Users\\Mooncat\\py\\TawianLab\\zip\\"+YEAR+"\\"

def to_int(m1):
    lst = []
    for i in range(len(m1)):
        a = m1[i][0:4]
        lst.append(int(a))
    return lst


def binary_search(data, key):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = int((low + high) / 2)
        if key == data[mid]:
            return mid
        elif key > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def get_txt(sym):
    s = ""
    with open(store_dir+str(sym)+".txt", 'r', encoding="utf-8") as f:
        for line in f.readlines():
            s += line
    return s

def get_cos(v1,v2):
    cos_sim = np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return cos_sim

def main_(set_,v=None):
    data_pool = os.listdir(PATH+YEAR) #準備全樣本
    s = sorted(list(set_)) #部分樣本代碼排序
    
    
    res = []
    if v is None:
        lst = []
        
        
    
    #取開頭4個字元 轉成int 以便搜尋
    for i in range(len(data_pool)):
        data_pool[i] = int(data_pool[i][0:4])
    
    for key in s:
        res = binary_search(data_pool, key) #二分法搜尋
        lst.append(res) #return index 【搜尋特定產業CSV】
    
    for w in lst:
        write_txt(data_pool[w], YEAR)
    

    # #一次取2個進行比較
    for idx in lst:
        for idx_ in lst:
            print(str(data_pool[idx])+"<--->"+str(data_pool[idx_]))
            s1 = get_txt(data_pool[idx])
            s2 = get_txt(data_pool[idx_])
            j1 = jieba_(s1)
            j2 = jieba_(s2)
            vector = tf_idf(j1,j2)
            cos = get_cos(vector[0], vector[1])
            
            with open("化學"+YEAR+".txt", "a+" )as f:
                f.write(str(data_pool[idx])+"<--->"+str(data_pool[idx_])+" : "+ str(cos)+"\n")
            

    
            
            
            
            

if __name__ == '__main__':
    m1 = os.listdir(PATH+YEAR) #全樣本
    m2 = pd.read_csv(PATH_SYMBOL+INDUSTRY) #部分樣本
    
    # 轉相同格式比對
    m1 = to_int(m1) 
    m2 = list(m2["代碼"])
    
    #交集
    set_ = set(m1) & set(m2)
    
    mains = main_(set_)