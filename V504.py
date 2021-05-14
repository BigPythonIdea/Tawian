# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:55:27 2021

.AAAAAAAAAAAAAAA
@author: Mooncat

V503 產業相似度 把各家"水泥" 產業 經由結巴 分完後 放入大樣本中 
去掉重複 打亂後 TF-IDF 算出相似度 結巴分出的結果存txt 

V504 jieba 那邊要想一下 然後想一下 用模組化的方式調整超參數 

V505 直接做兩樣本比對好了... 大樣本GG 優化雙迴圈 使執行變快
"""

import pandas as pd
import jieba
import os
import jieba.analyse

SYMBOL = "化學.csv"
ALL_YEAR = "2011"


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

def get_txt(number):
    df = pd.read_csv(".\zip\\"+ALL_YEAR+"\\"+str(number)+".csv")
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

def main_(set_,v=None):
    data_pool = os.listdir(".\zip\\"+ALL_YEAR) #準備全樣本
    s = sorted(list(set_)) #部分樣本代碼排序
    if v is None:
        lst = []
        txt_str = []
    
    #取開頭4個字元 轉成int 以便搜尋
    for i in range(len(data_pool)):
        data_pool[i] = int(data_pool[i][0:4])
       
    for key in s:
        res = binary_search(data_pool, key) #二分法搜尋
        lst.append(res) #index 搜尋特定產業CSV
    
    for index_ in lst:
        txt_str.append(get_txt(data_pool[index_]))  # get your string
    
    print(len(txt_str))
    # test = jieba_(str(txt_str[0]))
    # for i in test:
    #     print(i,end="")
        
    
        

m1 = os.listdir(".\zip\\"+ALL_YEAR) #全樣本
m2 = pd.read_csv(".\symbol\\"+SYMBOL) #部分樣本

# 轉相同格式比對
m1 = to_int(m1) 
m2 = list(m2["代碼"])

#交集
set_ = set(m1) & set(m2)

main_(set_)
