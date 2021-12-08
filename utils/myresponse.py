# @Time     :2021/11/4 10:44
# @Author   :dengyuting
# @File     :myresponse.py
from rest_framework.response import Response


class MyResponse(Response):

    def __init__(self, code=10000, msg='success', data='', status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super().__init__(data, status, template_name, headers, exception, content_type)

        self.data = {"code": code, "msg": msg, "data": data}
