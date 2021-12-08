# @Time     :2021/10/28 14:49
# @Author   :dengyuting
# @File     :testdb.py

import psycopg2

conn = psycopg2.connect(database="sg_storage_dev", user="dengyuting", password="dyt_123456", host="114.55.200.59", port="31543")
print("Opened database successfully")