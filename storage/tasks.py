# @Time     :2021/11/15 14:32
# @Author   :dengyuting
# @File     :tasks.py

# Create your tasks here
from celery.schedules import crontab
from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings

from myproject.celery import app
from .models import Companys

from celery import shared_task


@shared_task
def sendDingTalkmsg(msg):
    webhook = settings.DINGTALK_WEB_HOOK
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_text(msg)


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_companys():
    return Companys.objects.count()


@shared_task
def rename_companys(company_id, name):
    w = Companys.objects.get(id=company_id)
    w.name = name
    w.save()


@shared_task
def report():
    return 5


