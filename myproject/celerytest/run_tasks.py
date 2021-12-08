# @Time     :2021/11/15 10:22
# @Author   :dengyuting
# @File     :run_tasks.py

from tasks import add
result = add.delay(6, 4)

print('is task ready: %s' % result.ready())

run_result = result.get(timeout=1)
print('task result %s' % run_result)