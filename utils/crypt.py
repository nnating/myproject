# @Time     :2021/12/7 14:52
# @Author   :dengyuting
# @File     :crypt.py
import hashlib


def SHA1(password):
    sha = hashlib.sha1(password.encode('UTF-8'))
    encrypts = sha.hexdigest()
    return encrypts
