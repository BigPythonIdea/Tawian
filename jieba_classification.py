"""
Created on Sat Apr 17 10:28:05 2021
@author: Solana
"""

import pandas as pd
import jieba
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer


name = "汽車"

dt = pd.read_csv(name+".csv", index_col=0)
seqs = [[],[]]

for year in range(2011,2021):
    for t in dt["代碼"]:
        try:
            df = pd.read_csv("zip/"+str(year)+"/"+str(t)+".csv").to_string()
        except:
            print("path error"+str(t)+str(year))
            pass
        try:
            jieba.set_dictionary("dict.txt")
            df = df.replace(" ","").replace("。","").replace("Unnamed:","").replace("00","").replace("，","")
            tok = Tokenizer(num_words=None,
                filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
                lower=True, split=' ', char_level=False, oov_token=None,)
            lst = jieba.cut(df)
            st = []
            for i in lst:
                st.append(i)
            st = np.array(st)
            tok.fit_on_texts(st)
            seq = tok.texts_to_sequences(st)
            seqs[0].append(t)
            seqs[1].append(seq)
            
        except:
            print("jieba error"+str(t)+str(year))
    
    dd = pd.DataFrame(seqs).T
    dd.to_csv("C:\\Users\\Mooncat\\py\\Tawian\\"+name+"\\"+str(year)+".csv")



