# coding:utf-8
__author__ = 'Luo'

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from users.models import UserProfile


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        '''
        自定义用户验证
        :param request: 请求
        :param username: 用户名
        :param password: 密码
        :param kwargs: 一些参数
        :return: 返回该用户本身
        '''
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
