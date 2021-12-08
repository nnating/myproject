# @Time     :2021/12/7 16:43
# @Author   :dengyuting
# @File     :myauth.py
import time

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from jwtutils.utils import decode_jwt_token
from storage.models import Users


class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_Authorization'.upper())
        if not token:
            raise AuthenticationFailed('没有携带token')
        try:
            payload = decode_jwt_token(token)
        except Exception:
            raise AuthenticationFailed('异常token')
        user_no = payload['data']['user_no']
        password = payload['data']['password']
        exp = payload['exp']
        now = round(time.time())
        if exp > now:
            raise AuthenticationFailed('token过期')
        user = Users.objects.get(user_no=user_no, password=password)
        if not user:
            raise AuthenticationFailed('非法用户')
        return user, token
