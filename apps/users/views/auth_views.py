# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午5:43
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : auth_views.py
# @Software: PyCharm

from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from common.message_helper import genernal_message
from common.paginations import StandardPagination
from common.throttles import NormalAnonRateThrottle
from users.models import UserProfile, Permission
from users.serializers.auth_serializers import RegisterSerializer, PermissionSerializer, UserExtendInfoSerializer


class RegisterViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """
    用户注册
    """
    serializer_class = RegisterSerializer
    throttle_classes = (NormalAnonRateThrottle,)

    def get_queryset(self):
        return UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # 如果是抛异常，你就自己没法处理，所以这里让不抛异常自己处理不合法的异常
        headers = None
        if serializer.is_valid(raise_exception=False):
            user = self.perform_create(serializer)
            if user:
                # 生成payload
                payload = jwt_payload_handler(user)
                # 拿到序列化的数据
                re_dict = serializer.data
                headers = self.get_success_headers(re_dict)
                code, msg = status.HTTP_201_CREATED, "user register success"
                # 拼装一个 payload 进去
                re_dict["id"] = user.id
                re_dict["token"] = jwt_encode_handler(payload)
            else:
                re_dict, code, msg = {"error": "创建用户失败"}, status.HTTP_400_BAD_REQUEST, "user register failed"
        else:
            re_dict, code, msg = serializer.errors, status.HTTP_400_BAD_REQUEST, "user register failed"
        result = genernal_message(code=code, msg=msg, data=re_dict)
        return Response(result, status=code, headers=headers)

    def perform_create(self, serializer):
        """
        返回 user 对象，为了生成 Token
        :param serializer: 序列化器
        :return: 返回 user 对象
        """
        return serializer.save()


class UserExtendInfoViewSet(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = UserExtendInfoSerializer
    lookup_field = "user_id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        code = status.HTTP_200_OK
        re_dict = serializer.data
        re_dict["username"] = request.user.username
        re_dict["email"] = request.user.email
        result = genernal_message(code=code, msg="数据获取成功", data=re_dict)
        return Response(data=result, status=code)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        code, re_dict = status.HTTP_200_OK, dict()
        if serializer.is_valid(raise_exception=False):
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            msg, re_dict = "数据修改成功", serializer.data
        else:
            code, msg = status.HTTP_400_BAD_REQUEST, "数据修改失败"
        result = genernal_message(code=code, msg=msg, data=re_dict)
        return Response(result)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class PermissionViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = PermissionSerializer
    pagination_class = StandardPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            perm = self.perform_create(serializer)
            if perm:
                re_dict = serializer.data
                code, msg = status.HTTP_201_CREATED, "add permission success"
                re_dict["id"] = perm.id
            else:
                re_dict, code, msg = {"error": "创建权限失败"}, status.HTTP_400_BAD_REQUEST, "add permission failed"
        else:
            re_dict, code, msg = serializer.errors, status.HTTP_400_BAD_REQUEST, "add permission failed"
        result = genernal_message(code=code, msg=msg, data=re_dict)
        return Response(result, status=code)

    def perform_create(self, serializer):
        """
        返回 Obj 对象
        :param serializer: 序列化器
        :return: 返回 Obj 对象
        """
        return serializer.save()

    def get_queryset(self):
        return Permission.objects.get_obj_list(
            e_kwargs={
                "is_delete": 1
            }
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # 这里会对数据做一些处理，关于数据总数上一页下一页...
            response = self.get_paginated_response(serializer.data)
            result = genernal_message(code=status.HTTP_200_OK, msg="权限列表返回成功", data=response.data)
            response.data = result
        else:
            serializer = self.get_serializer(queryset, many=True)
            result = genernal_message(code=status.HTTP_200_OK, msg="权限列表返回成功", data=serializer.data)
            response = Response(data=result)
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance = self.perform_destroy(instance)
        code, msg = (status.HTTP_200_OK, "权限删除成功") if isinstance(instance.is_delete,
                                                                 int) and instance.is_delete == 1 else (
        status.HTTP_400_BAD_REQUEST, "权限删除失败")
        result = genernal_message(code=code, msg=msg)
        return Response(data=result, status=code)

    def perform_destroy(self, instance):
        instance.is_delete = 1
        instance.save()
        return instance

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        code = status.HTTP_200_OK
        result = genernal_message(code=code, msg="数据获取成功", data=serializer.data)
        return Response(data=result, status=code)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        code, re_dict = status.HTTP_200_OK, dict()
        if serializer.is_valid(raise_exception=False):
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            msg, re_dict = "数据修改成功", serializer.data
        else:
            code, msg = status.HTTP_400_BAD_REQUEST, "数据修改失败"
        result = genernal_message(code=code, msg=msg, data=re_dict)
        return Response(result)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
