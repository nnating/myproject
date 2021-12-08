# @Time     :2021/11/15 10:13
# @Author   :dengyuting
# @File     :tasks.py

from celery import Celery

app = Celery('tasks', backend='redis://192.168.100.222:61379', broker='redis://192.168.100.222:61379')

@app.task
def add(x, y):
    return x + y