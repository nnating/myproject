# @Time     :2021/12/7 17:15
# @Author   :dengyuting
# @File     :myperm.py
from rest_framework.permissions import BasePermission


class MyPerm(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return True
        return False
