import requests
from bs4 import BeautifulSoup
import pandas as pd

import requests
import pandas as pd

url = "https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=1&issuetype=1&industry_code=&Page=1&chklike=Y"
response = requests.get(url)

dfs = pd.read_html(response.text)
stock_code = dfs[0][2][1:].tolist()
stock_name = dfs[0][3][1:].tolist()
stock_industry = dfs[0][6][1:].tolist()

import datetime
import pymysql

# 資料庫連線設定
host = "localhost"
user = "root"
password = "123456"
database = "stockdb"

# 資料庫連線建立
conn = pymysql.connect(host=host, user=user, password=password, database=database)

cursor = conn.cursor()

# 將股票資訊寫入 stock 資料表中
for i in range(len(stock_code)):
    code = stock_code[i]
    name = stock_name[i]
    industry = stock_industry[i]
    cursor.execute('''
    INSERT INTO stock(code, name, industry) VALUES (%s, %s, %s)
    ''', (code, name, industry))

# 提交資料庫變更，關閉資料庫連接
conn.commit()
conn.close()


