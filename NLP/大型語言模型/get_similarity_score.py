import pymysql
import numpy as np
import pandas as pd
import re
from ckip_transformers.nlp import CkipWordSegmenter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 資料庫連線設定
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='stockdb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 輸入查詢的公司代碼和年度
company_code = input("======輸入查詢的公司代碼======\n")
year = input("======輸入查詢年度======\n")

def query_by_id(company_id):
    try:
        with connection.cursor() as cursor:
            # 執行 SQL 查詢
            sql = "SELECT * FROM quarterly_reports WHERE company_code = %s"
            cursor.execute(sql, (company_id,))
            result = cursor.fetchall()

            if result:
                return pd.DataFrame(result)
            else:
                print("找不到該 ID 的資料")
    except pymysql.Error as e:
        print(f"查詢發生錯誤：{e}")

# 查詢指定公司代碼的資料
df = query_by_id(company_code)

quarters = ["01", "02", "03", "04"]
years = [year]

# 篩選指定年度和季度的資料
result = df[df['quarter_date'].isin(quarters) & df['year'].isin(years)]

def clear(content):
    # 移除全形空格和換行符號
    result_str = ''.join(word for word in content if word not in ['\u3000', '\n'])
    
    # 移除標點符號和空格
    result_str = re.sub(r'[^\w\s]', '', result_str)
    result_str = re.sub(r'\s+', '', result_str)

    return result_str

# 清理內容欄位
result['content'] = result['content'].apply(clear)

ws_driver = CkipWordSegmenter(model="bert-base")

def word_segmentation(content):
    words = ws_driver([content])[0]
    return ' '.join(words)

# 對 content 欄位進行斷詞
result['content'] = result['content'].apply(word_segmentation)

# 取得不同季度的斷詞內容
t1 = ' '.join(result.loc[result['quarter_date'] == "01", 'content'])
t2 = ' '.join(result.loc[result['quarter_date'] == "02", 'content'])
t3 = ' '.join(result.loc[result['quarter_date'] == "03", 'content'])
t4 = ' '.join(result.loc[result['quarter_date'] == "04", 'content'])

def cosine_similarity_score(x, y):
    documents = [x, y]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_score = cosine_similarity(tfidf_matrix)[0, 1]
    print(f"相似度分數: {round(similarity_score * 100, 2)} %")

# 計算相似度分數
ct21 = cosine_similarity_score(t2, t1)
ct32 = cosine_similarity_score(t3, t2)
ct43 = cosine_similarity_score(t4, t3)
