# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午6:52
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : auth_serializers.py
# @Software: PyCharm

from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from common.exceptions import CreateObjectError
from users.models import UserProfile, UserExtendInfo, Permission


class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=True,
        allow_blank=False,
        label="用户名",
        validators=[UniqueValidator(
            queryset=UserProfile.objects.all(),
            message="用户名已存在"
        )]
    )

    email = serializers.CharField(
        required=True,
        allow_blank=False,
        label="邮箱",
        validators=[UniqueValidator(
            queryset=UserProfile.objects.all(),
            message="邮箱已存在"
        )]
    )

    password = serializers.CharField(
        min_length=8,
        max_length=16,
        style={"input_type": "password"},
        label="请输入密码",
        write_only=True,  # 需要你填写，但是不会被序列化返回到前端
    )

    password_repeat = serializers.CharField(
        min_length=8,
        max_length=16,
        style={"input_type": "password"},
        label="请重复输入密码",
        write_only=True,  # 需要你填写，但是不会被序列化返回到前端
    )

    def validate(self, attrs):
        # 删除多余的字段，防止报错
        del attrs["password_repeat"]
        return attrs

    class Meta:
        fields = ("username", "email", "password", "password_repeat")
        model = UserProfile
        # 这个类有多少字段就需要写多少字段在这

    @transaction.atomic
    def create(self, validated_data):
        '''
        重写这个是为了让密码变成密文
        :param validated_data: 验证过后的字段
        :return: 返回创建的对象
        '''
        save_id = transaction.savepoint()
        try:
            user = super(RegisterSerializer, self).create(validated_data=validated_data)
            user.set_password(validated_data["password"])
            user.save()
            UserExtendInfo.objects.create_one_obj(db_select=None, create_info={"user_id": user.id})
        except Exception as e:   # 用户拓展信息表的错误
            transaction.savepoint_rollback(save_id)
            raise CreateObjectError("创建用户拓展信息失败")
        transaction.savepoint_commit(save_id)
        return user


class PermissionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        allow_blank=False,
        label="权限名",
        validators=[UniqueValidator(
            queryset=Permission.objects.all(),
            message="权限已存在"
        )]
    )

    desc = serializers.CharField(
        required=True,
        allow_blank=False,
        label="权限描述"
    )

    class Meta:
        model = Permission
        fields = ("name", "desc")


class UserExtendInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtendInfo
        fields = ("name", "desc")