# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午5:48
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : message_helper.py
# @Software: PyCharm


def genernal_message(code, msg, data):
    info = {
        "msg": msg,
        "code": code,
        "data": data
    }
    return info
