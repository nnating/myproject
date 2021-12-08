# @Time     :2021/10/28 14:56
# @Author   :dengyuting
# @File     :serializers.py
import datetime

from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from storage.models import Companys, Users, Galleries, File, Roles


class CompanysSerializer(serializers.ModelSerializer):
    """
    序列化，能够将表数据，转换为json字典以及json字符串
    """

    company_id = serializers.IntegerField(required=False)
    ##设置了没用
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Companys
        fields = ('company_id', 'company_name', 'company_logo', 'system_name', 'created_at', 'updated_at', 'deleted_at')
        #设置了没用
        read_only_fields = ('company_id', 'created_at')

    def update(self, instance, validated_data):
        if 'created_at' in validated_data.keys():
            validated_data.pop('created_at')
        updated_at = datetime.datetime.now()
        validated_data['updated_at'] = str(updated_at)
        ##serializers.ModelSerializer 是父类；super().update继承父类的方法
        company = super().update(instance, validated_data)
        company.save()
        return company


class UsersSerializer(serializers.ModelSerializer):

    days_since_joined = serializers.SerializerMethodField()

    def get_days_since_joined(self, obj):
        return (now() - obj.created_at).days

    class Meta:
        # 指定一个Model，根据该model自动检测序列化的字段
        model = Users
        #所有模型字段都将映射到相应的序列化程序字段
        # fields = '__all__'
        #可指定要包含的字段，可以使用fields或exclude选项
        fields = ['user_id', 'user_no', 'user_name', 'mobile', 'days_since_joined']
        # exclude = ['password']



class GalleriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Galleries
        fields = '__all__'


##使用ModelSerializer对象
##ModelSerializer对象不需要重复很多包含在File模型（model）中的字段信息
class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'remark', 'timestamp')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']



#使用Serializer对象
class RolesSerializer(serializers.Serializer):
    #定义了需要序列化的字段
    role_id = serializers.IntegerField(read_only=True)
    role_name = serializers.CharField(allow_blank=True, allow_null=True, max_length=100)
    description = serializers.CharField(allow_blank=True, max_length=100, default='这是一个角色的描述')
    permissions = serializers.CharField(allow_blank=True, required=False, allow_null=True)  # This field type is a guess.
    role_type = serializers.IntegerField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    deleted_at = serializers.DateTimeField(required=False, write_only=True)


    #在反序列化时，当save()调用时生成对象Role
    def create(self, validated_data):
        # 会将生成的实例保存到数据库
        return Roles.objects.create(**validated_data)


    #在反序列化时，当save()调用时更新对象Role
    def update(self, instance, validated_data):
        instance.role_name = validated_data.get('role_name', instance.role_name)
        instance.description = validated_data.get('description', instance.description)
        updated_at = datetime.datetime.now()
        instance.updated_at = str(updated_at)
        #保存在数据库中
        instance.save()
        return instance

