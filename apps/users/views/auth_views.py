# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午5:43
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : auth_views.py
# @Software: PyCharm

from rest_framework import mixins, status
from rest_framework.response import Response

from common.base_view import BaseApiView
from common.message_helper import genernal_message
from users.serializers.auth_serializers import RegisterSerializer


class RegisterView(BaseApiView, mixins.CreateModelMixin):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # 如果是抛异常，你就自己没法处理，所以这里让不抛异常自己处理不合法的异常
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            result = genernal_message(code=status.HTTP_201_CREATED, msg="register success", data=serializer.data)
            return Response(result, status=status.HTTP_201_CREATED, headers=headers)
        else:
            err = serializer.errors
            result = genernal_message(code=status.HTTP_400_BAD_REQUEST, msg="register failed", data=err)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # 会调用 Serializer 的 create 或者 update 方法，然后调用 Model 的 create 或者 update
        serializer.save()   # 用的是 create 或者 update 方法的返回值

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

