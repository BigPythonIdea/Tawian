import pymysql
import numpy as np
import pandas as pd
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



