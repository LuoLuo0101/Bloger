# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午1:33
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : exceptions.py
# @Software: PyCharm


class CustomException(Exception):
    def __init__(self, message):
        super(CustomException, self).__init__(message)


class ObjectNotExistError(CustomException):
    """
    对象不存在
    """
    pass


class MultipleObjectsReturnedError(CustomException):
    """
    获取到多个对象
    """


class CreateObjectError(CustomException):
    """
    创建对象失败
    """


class CreateInfoEmptyError(CustomException):
    """
    创建对象的参数为空
    """


class DeleteObjectError(CustomException):
    """
    删除对象失败
    """


class UpdateObjectError(CustomException):
    """
    更新对象失败
    """