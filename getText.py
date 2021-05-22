# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:31:10 2021

@author: Mooncat
"""

def  get_txt(sym,sym1):
    s1 = ""
    with open(sym+".txt", 'r', encoding="utf-8") as f:
        for line in f.readlines():
            s1 += line
            
    s2 = ""
    with open(sym1+".txt", 'r', encoding="utf-8") as f1:
        for line in f1.readlines():
            s2 += line
    
    return s1, s2
    
    