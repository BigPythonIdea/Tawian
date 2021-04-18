import pandas as pd
import jieba
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer




df = pd.read_csv("zip/2011/1101.csv").to_string()

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
print(seq)
