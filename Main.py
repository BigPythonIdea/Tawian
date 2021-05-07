# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:55:18 2021

@author: Mooncat
"""

import pandas as pd
import jieba
import os

SYMBOL = "化學.csv"  #指定樣本
ALL_YEAR = "2011"   #全樣本
INPUT_A = "" # A ↔ B
INPUT_B = "" # B ↔ A

def to_int(all_year_sample):
    lst = []
    for i in range(len(all_year_sample)):
        a = all_year_sample[i][0:4]
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


def search(set_, all_sample, v=None):
    if v is None:
        index_list = []

    data_pool = all_sample
    sort_ = sorted(list(set_)) #部分樣本代碼排序
    
    # 全樣本中二分搜尋特定產業
    for key in sort_:
        res = binary_search(data_pool, key) #二分法搜尋
        index_list.append(res) #接收回傳index
        
    return index_list

def get_txt(symbol):
    df = pd.read_csv(".\zip\\"+ALL_YEAR+"\\"+str(symbol)+".csv")
    word = list(df["0"])
    outstr = ' '.join(str(e) for e in word)
    return outstr

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def jieba_(lst,v=None):
    jieba.set_dictionary("dict.txt")
    jie = jieba.cut(lst)
    stop = stopwordslist("stop.txt")
    outstr = ''
    for word in jie:
        if word not in stop:
            if word != '\n' and word!=" ":
                outstr += word
                outstr += "-"
    return outstr

    


if __name__ == '__main__':
    m1 = os.listdir(".\zip\\"+ALL_YEAR) #全樣本
    m2 = pd.read_csv(".\symbol\\"+SYMBOL) #部分樣本
    
    m1 = to_int(m1) 
    m2 = list(m2["代碼"])
    
    set_ = set(m1) & set(m2)
    
    index_list = search(set_,m1) # 回收特定CSV 的 index
    
    for a in index_list:
        for b in index_list:
            if a != b:
                t1 = get_txt(m1[a])
                t2 = get_txt(m1[b])
                
                j1 = jieba_(t1)
                j2 = jieba_(t2)
                
                print(j1,j2,end="")
                break
    
