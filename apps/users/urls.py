# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午5:44
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from users.views.auth_views import RegisterViewSet, PermissionViewSet

router = DefaultRouter()
router.register(prefix="register", viewset=RegisterViewSet, base_name="register")
router.register(prefix="permission", viewset=PermissionViewSet, base_name="permission")

urlpatterns = [
    # router 解释根路由
    url(r'^', include(router.urls)),
]
