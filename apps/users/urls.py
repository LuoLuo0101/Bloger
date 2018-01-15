# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午5:44
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from users.views.auth_views import RegisterView

urlpatterns = [
    url("^register/?", RegisterView.as_view(), name="register")
]
