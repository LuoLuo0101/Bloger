# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午5:24
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : base_view.py
# @Software: PyCharm

from datetime import datetime

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView, jwt_response_payload_handler

from common.message_helper import genernal_message


class BaseApiView(GenericAPIView):
    """
        任何人可以访问

        没有权限限制
    """
    permission_classes = (AllowAny,)

    def __init__(self, *args, **kwargs):
        super(BaseApiView, self).__init__(*args, **kwargs)


class BaseJWTAuthApiView(GenericAPIView):
    """
        JWT 登录验证

        JWT 登录用户才可以访问
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def __init__(self, *args, **kwargs):
        super(BaseJWTAuthApiView, self).__init__(*args, **kwargs)


class JWTTokenView(JSONWebTokenAPIView):
    """
        JWT 登录验证的 View

        重定义了 JWT 认证
    """
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            result = genernal_message(code=status.HTTP_200_OK, msg="login success", data=response_data)
            response = Response(data=result, status=status.HTTP_200_OK)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=expiration, httponly=True)
            return response
        err = serializer.errors
        err_info = {"error": list(err.values())[0]}
        result = genernal_message(code=status.HTTP_400_BAD_REQUEST, msg="login failed", data=err_info)
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
