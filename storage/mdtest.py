# @Time     :2021/11/5 14:28
# @Author   :dengyuting
# @File     :mdtest.py

from django.utils.deprecation import MiddlewareMixin#
from django.shortcuts import HttpResponse

class Md1(MiddlewareMixin):

    def process_request(self, request):
        print("Md1请求")
        return HttpResponse("Md1中断")

    def process_response(self, request, response):
        print("Md1返回")
        return response

class Md2(MiddlewareMixin):

    def process_request(self,request):
        print("Md2请求")
        # return HttpResponse("Md2中断")

    def process_response(self,request,response):#
        print("Md2返回")
        return response
