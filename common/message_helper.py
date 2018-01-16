# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午5:48
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : message_helper.py
# @Software: PyCharm

from rest_framework import status


def genernal_message(code=status.HTTP_200_OK, msg="", data=None):
    if not isinstance(data, dict):
        data = dict()
    info = {
        "msg": msg,
        "code": code,
        "data": data
    }
    return info
