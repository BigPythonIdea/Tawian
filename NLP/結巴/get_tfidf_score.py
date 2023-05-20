import pymysql
import numpy as np
import pandas as pd
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker
from sklearn.feature_extraction.text import TfidfVectorizer


def connect_database():
    host = "localhost"
    user = "root"
    password = "123456"
    database = "stockdb"

    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute('SELECT company_code, quarter_date, content, year FROM quarterly_reports')
    result = cursor.fetchall()
    conn.close()
    return result

# connect = [connect_database()]
# get_content1 = connect[0][1][2]
# get_content2 = connect[0][2][2]
# get_content3 = connect[0][3][2]
# get_content4 = connect[0][4][2]

# q1 = segment(get_content1, "./NLP/stop.txt")
# q2 = segment(get_content2, "./NLP/stop.txt")
# q3 = segment(get_content3, "./NLP/stop.txt")
# q4 = segment(get_content4, "./NLP/stop.txt")

connect = [connect_database()]
get_content1 = connect[0][1][2]
result_str = ''
for word in get_content1:
    if word == '\u3000' or word == '\n':
        continue
    result_str += word

df = pd.DataFrame([])

# Initialize drivers
print("Initializing drivers ... WS")
# device=0 為使用gpu進行運算，如電腦無gpu者可改為 device=-1 用cpu運算
ws_driver = CkipWordSegmenter(model="albert-base", device=0)
print("Initializing drivers ... POS")
pos_driver = CkipPosTagger(model="bert-base", device=0)
print("Initializing drivers ... NER")

df["seg"] = list(map(lambda x: ws_driver([x]), result_str))
df["seg"] = df["seg"].apply(lambda x : x[0])
df["pos"] = df["seg"].apply(lambda x : pos_driver(x))

