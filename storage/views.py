import time

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from jwtutils.utils import get_jwt_token, decode_jwt_token
from storage.models import Companys, Users, Galleries, File, Roles
from storage.serializers import CompanysSerializer, UsersSerializer, GalleriesSerializer, FileSerializer, RolesSerializer

import logging

# 生成一个以当前文件名为名字的logger实例
from storage.tasks import count_companys, sendDingTalkmsg
from utils.crypt import SHA1
from utils.myresponse import MyResponse

logger = logging.getLogger(__name__)


@api_view(['POST'])
##设置了全局的认证与权限，但是登录接口要禁用认证和权限
@permission_classes((AllowAny,))
@authentication_classes(())
def login(request):
    data = JSONParser().parse(request)
    user_no = data.get('user_no')
    password = SHA1(data.get('password'))
    try:
        user = Users.objects.get(user_no=user_no, password=password)
    except Users.DoesNotExist:
        errorInfo = '用户名或密码错误'
        return MyResponse(code=10001, msg=errorInfo, data="", status=301)
    token = get_jwt_token(user_no=user_no, password=password)
    token_dict = {'token': token}
    return MyResponse(data=token_dict)


# @api_view(['POST'])
# ##设置了全局的认证与权限，但是登录接口要禁用认证和权限
# @permission_classes((AllowAny,))
# @authentication_classes(())
# def login(request):
#     data = JSONParser().parse(request)
#     username = data.get('username')
#     password = data.get('password')
#     #调用django进行用户认证,验证成功 user返回,验证失败 user返回None
#     # user = auth.authenticate(username=username, password=password)
#     try:
#         user = auth.authenticate(username=username, password=password)
#         payload = jwt_payload_handler(user)
#         token = jwt_encode_handler(payload)
#         token_dict = {'token': token}
#         return MyResponse(data=token_dict)
#     except Exception:
#         errorInfo = '用户名或密码错误'
#         return MyResponse(code=10001, msg=errorInfo, data="", status=301)


# @api_view(['POST'])
# ##设置了全局的认证与权限，但是登录接口要禁用认证和权限
# @permission_classes((AllowAny,))
# @authentication_classes(())
# def login(request):
#     data = JSONParser().parse(request)
#     username = data.get('username')
#     password = data.get('password')
#     #调用django进行用户认证,验证成功 user返回,验证失败 user返回None
#     user = auth.authenticate(username=username, password=password)
#     if user == None:
#         errorInfo = '用户名或密码错误'
#         return MyResponse(code=10001, msg=errorInfo, data="", status=301)
#     # 用户名和密码验证成功
#     # 获取用户的token 如果没有token ，表示时用户首次登录，则进行创建，并且返回token
#     try:
#         tokenObj = Token.objects.get(user_id=user.id)
#     except Exception as e:
#         # token 不存在 说明是首次登录
#         tokenObj = Token.objects.create(user=user)
#     # 获取token字符串
#     token = tokenObj.key
#     token_dict = {'token': token}
#     print(request.user)
#     print(request.auth)
#     sendDingTalkmsg.delay('hello: %s welcome to mmm company' % username)
#     return MyResponse(data=token_dict)


##基于函数的视图
@api_view(['GET', 'POST'])
# @permission_classes((AllowAny,))
def companyslist(request):

    if request.method == 'GET':
        # 实例化分页器对象
        page = PageNumberPagination()
        companys = Companys.objects.all()
        count_companys.delay()
        # 调用分页方法去分页查询结果集
        ret = page.paginate_queryset(companys, request)
        # 分页好的数据序列化，序列化，是指将复杂的QuerySet和Model类型转换成Python基本数据类型，从而将这些基本数据类型以JSON的形式响应给客户端
        serializer = CompanysSerializer(ret, many=True)
        return MyResponse(data=serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        #反序列化则和序列化相反，是指将Http请求中传入的JSON数据转换成复杂的数据类型，从而保存在数据库中。
        serializer = CompanysSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return MyResponse(data=serializer.data, status=201)
        logger.error(serializer.errors)
        return MyResponse(code=10002, msg=serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        company = Companys.objects.get(pk=pk)
    except Companys.DoesNotExist:
        logger.error(Companys.DoesNotExist)
        return MyResponse(code=10002, msg='数据不存在', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanysSerializer(company)
        return MyResponse(data=serializer.data)

    elif request.method == 'PUT':
        serializer = CompanysSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.update(instance=company, validated_data=request.data)
            return MyResponse(data=serializer.data)
        logger.error(serializer.errors)
        return MyResponse(msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return MyResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def userslist(request):
    print(request.version)
    if request.method == 'GET':
        #实例化分页器对象
        page = PageNumberPagination()
        users = Users.objects.all()
        #调用分页方法去分页查询结果集
        ret = page.paginate_queryset(users, request)
        #分页好的数据序列化
        serializer = UsersSerializer(ret, many=True)
        logger.error(serializer.data)
        return MyResponse(data=serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return MyResponse(data=serializer.data, status=201)
        logger.error(serializer.errors)
        return MyResponse(code=10002, msg=serializer.errors, status=400)


@api_view(['GET', 'POST'])
def gallerieslist(request):
    if request.method == 'GET':
        #实例化分页器对象
        page = PageNumberPagination()
        galleries = Galleries.objects.all()
        #调用分页方法去分页查询结果集
        ret = page.paginate_queryset(galleries, request)
        #分页好的数据序列化
        serializer = GalleriesSerializer(ret, many=True)
        return MyResponse(data=serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GalleriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return MyResponse(data=serializer.data, status=201)
        logger.error(serializer.errors)
        return MyResponse(code=10002, msg=serializer.errors, status=400)



@api_view(['POST'])
def upload(request):
    if request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return MyResponse(data=serializer.data, status=201)
        logger.error(serializer.errors)
        return MyResponse(code=10002, msg=serializer.errors, status=400)


@api_view(['GET'])
def fileslist(request):
    if request.method == 'GET':
        #实例化分页器对象
        page = PageNumberPagination()
        file = File.objects.all()
        #调用分页方法去分页查询结果集
        ret = page.paginate_queryset(file, request)
        #分页好的数据序列化
        serializer = FileSerializer(ret, many=True)
        return MyResponse(data=serializer.data)


@api_view(['GET'])
def index(request):

    print("view函数...")
    return HttpResponse('OK')


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def roleslist(request):
    if request.method == 'GET':
        page = PageNumberPagination()
        roles = Roles.objects.all()
        ret = page.paginate_queryset(roles, request)
        # 分页好的数据序列化
        serializer = RolesSerializer(ret, many=True)
        ##serializer.data 将model转化为python类型，serializer.data中保存了序列化后的数据
        return MyResponse(data=serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RolesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return MyResponse(data=serializer.data, status=201)
        logger.error(serializer.errors)
        return MyResponse(code=10002, msg=serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        role = Roles.objects.get(pk=pk)
    except Roles.DoesNotExist:
        logger.error(Roles.DoesNotExist)
        return MyResponse(code=10002, msg='数据不存在', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RolesSerializer(role)
        return MyResponse(data=serializer.data)

    elif request.method == 'PUT':
        serializer = RolesSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.update(instance=role, validated_data=request.data)
            return MyResponse(data=serializer.data)
        logger.error(serializer.errors)
        return MyResponse(msg=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        role.delete()
        return MyResponse(status=status.HTTP_204_NO_CONTENT)
