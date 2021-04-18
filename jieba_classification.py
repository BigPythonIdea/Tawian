import pandas as pd
import jieba
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer



dt = pd.read_csv("光電.csv", index_col=0)
seqs = [[],[]]
for t in dt["代碼"]:
    try:
        df = pd.read_csv("zip/2011/"+str(t)+".csv").to_string()
    except:
        pass

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
