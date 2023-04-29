import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pymysql
import time

# 資料庫連線設定
host = "localhost"
user = "root"
password = "123456"
database = "stockdb"

data = []
names = []
# 資料庫連線建立
conn = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
cursor.execute('SELECT * FROM stock')
result = cursor.fetchall()
# 將每一行資料轉換成字典型別，並顯示出來
for row in result:
    data.append(row[0])
    names.append(row[1])
# 關閉資料庫連接
conn.close()
data = [int(x) for x in data]

for symbol in data:
    driver = webdriver.Chrome()
    driver.get("https://mops.twse.com.tw/mops/web/t163sb03")
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="isnew"]'))
        select.select_by_value("false")

        element = driver.find_element(By.XPATH, '//*[@id="co_id"]')
        element.send_keys(str(symbol))

        year = driver.find_element(By.XPATH, '//*[@id="year"]')
        year.send_keys("109")

        season = Select(driver.find_element(By.XPATH, '//*[@id="season"]'))
        season.select_by_value("01")

        button = driver.find_element(By.XPATH, '/html/body/center/table/tbody/tr/td/div[4]/table/tbody/tr/td/div/table/tbody/tr/td[3]/div/div[3]/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div/input').click()
    except Exception as e:
        print(str(symbol))
        print(e)
    time.sleep(3)
    content = driver.find_element(By.XPATH, '//*[@id="table01"]/table[4]/tbody/tr[4]/td/pre').text

    print(content)

    
    #driver.close()
    break

