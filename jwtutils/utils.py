# @Time     :2021/12/7 13:57
# @Author   :dengyuting
# @File     :utils.py
import datetime

import jwt
from django.conf import settings


def get_jwt_token(user_no, password):
    payload = {
        'exp': datetime.datetime.now() + datetime.timedelta(days=1),
        'iat': datetime.datetime.now(),
        'data': {
            'user_no': user_no,
            'password': password
        }
    }

    encode_jwt = jwt.encode(payload, key=settings.SECRET_KEY, algorithm='HS256')
    return str(encode_jwt, encoding='UTF-8')


def decode_jwt_token(token):
    s = jwt.decode(token, key=settings.SECRET_KEY, algorithm='HS256')
    return s

