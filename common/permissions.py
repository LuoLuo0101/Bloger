# coding:utf-8
__author__ = 'Luo'

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    不是作者只能查看
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
