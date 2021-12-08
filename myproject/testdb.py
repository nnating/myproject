# @Time     :2021/10/28 14:49
# @Author   :dengyuting
# @File     :testdb.py

import psycopg2

conn = psycopg2.connect(database="sg_storage_dev", user="test", password="123456", host="192.168.100.222", port="31543")
print("Opened database successfully")