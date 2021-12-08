# @Time     :2021/11/15 13:50
# @Author   :dengyuting
# @File     :celery.py

#celery -A myproject beat -l INFO
# celery -A myproject worker --loglevel=INFO -P gevent
#celery -A myproject flower --broker=redis://@192.168.100.222:61379/1



import os
from datetime import timedelta

from celery import Celery

# Set the default Django settings module for the 'celerytest' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celerytest-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, mytest.s('hello'), name='add every 10')
    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, mytest.s('world'), expires=10)
    # # Executes every Monday morning at 7:30 a.m.
    # # sender.add_periodic_task(
    # #     crontab(hour=7, minute=30, day_of_week=1),
    # #     test.s('Happy Mondays!'),
    # # )
    # sender.add_periodic_task(
    #     crontab(hour=14, minute=22, day_of_week=2),
    #     mytest.s('Happy Tuesday!'),
    # )

app.conf.update(CELERYBEAT_SCHEDULE =
                {
                    'sum-task': {'task': 'storage.tasks.add',
                                        'schedule': timedelta(seconds=22),
                                        'args': (5, 6)
                                },
                    'send-report': {
                                'task': 'storage.tasks.report',
                                'schedule': crontab(hour=17, minute=18, day_of_week=2),
                                }
                 }
                )

@app.task
def mytest(arg):
    print(arg)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')