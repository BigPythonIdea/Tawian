# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:55:27 2021

@author: Mooncat

V503 產業相似度 把各家"水泥" 產業 經由結巴 分完後 放入大樣本中 
去掉重複 打亂後 TF-IDF 算出相似度 結巴分出的結果存txt 

V504 jieba 那邊要想一下 然後想一下 用模組化的方式調整超參數 
"""

import pandas as pd
import jieba
import os
import jieba.analyse
import jieba.posseg as pseg

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

def get_txt(number,v=None):
    df = pd.read_csv(".\zip\\"+ALL_YEAR+"\\"+str(number)+".csv")
    outstr = ""
    for word in df["0"]:
        if word != '\n':
            outstr += word
 
    return outstr


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def jieba_(lst,v=None):
    in_str= ''
    for idx in range(len(lst)):
        in_str = str(lst[idx]) 
        
    jieba.set_dictionary("dict.txt")
    jie = jieba.cut(in_str)
    stop = stopwordslist("stop.txt")
    outstr = ''
    for word in jie:
        if word not in stop:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

def main_(set_,v=None):
    data_pool = os.listdir(".\zip\\"+ALL_YEAR)
    s = sorted(list(set_))
    if v is None:
        lst = []
        st = []
        
    for i in range(len(data_pool)):
        data_pool[i] = int(data_pool[i][0:4])
        
    for key in s:
        res = binary_search(data_pool, key)
        lst.append(res) #index 搜尋特定產業CSV
    
    for index_ in lst:
        txt = get_txt(data_pool[index_]) # get your string
        st.append(txt)
    
    get_jieba = list(jieba_(st))
    print(get_jieba,end="")
    
    # outstr = ""
    # for i in get_jieba:
    #     if i != " ":
    #         outstr += str(i)
    # print(outstr)
    

m1 = os.listdir(".\zip\\"+ALL_YEAR)
m2 = pd.read_csv(".\symbol\\"+SYMBOL)

m1 = to_int(m1)
m2 = list(m2["代碼"])

set_ = set(m1) & set(m2)

l = main_(set_)
