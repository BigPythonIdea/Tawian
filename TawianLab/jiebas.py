# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:09:38 2021

@author: Mooncat
"""

import jieba



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
                
    return outstr