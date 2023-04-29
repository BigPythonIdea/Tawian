from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pymysql
import time


def connect_database():
    host = "localhost"
    user = "root"
    password = "123456"
    database = "stockdb"

    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stock')
    result = cursor.fetchall()
    conn.close()
    return result

def insert_report_to_database(code, name, content, year, season):
    host = "localhost"
    user = "root"
    password = "123456"
    database = "stockdb"

    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO financial_report (code, name, content, year, season) VALUES (%s, %s, %s, %s, %s)', (code, name, content, year, season))
    conn.commit()
    conn.close()


def get_report_content(symbol, year, season):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get("https://mops.twse.com.tw/mops/web/t163sb03")

    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="isnew"]'))
        select.select_by_value("false")

        element = driver.find_element(By.XPATH, '//*[@id="co_id"]')
        element.send_keys(str(symbol))

        year_field = driver.find_element(By.XPATH, '//*[@id="year"]')
        year_field.clear() # 先清空欄位內容
        year_field.send_keys(str(year))

        season_select = Select(driver.find_element(By.XPATH, '//*[@id="season"]'))
        season_select.select_by_value(str(season))

        search_button = driver.find_element(By.XPATH, '/html/body/center/table/tbody/tr/td/div[4]/table/tbody/tr/td/div/table/tbody/tr/td[3]/div/div[3]/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div/input').click()
    except Exception as e:
        print(str(symbol))
        print(e)
        driver.quit()
        return ""

    time.sleep(3)
    try:
        content = driver.find_element(By.XPATH, '//*[@id="table01"]/table[4]/tbody/tr[4]/td/pre').text
    except Exception as e:
        content = ""
        print(str(symbol) + " - No Data")

    driver.quit()
    return content


def main():
    result = connect_database()
    symbols = [row[0] for row in result]
    symbols = list(map(int, symbols))

    years = ['109','110','110']
    seasons = ['01', '02', '03', '04']

    for year in years:
        for season in seasons:
            for symbol in symbols:
                content = get_report_content(symbol, year, season)
                if content:
                    print("I get content")



if __name__ == '__main__':
    main()
