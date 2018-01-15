# coding:utf-8
__author__ = 'Luo'
from enum import Enum, unique


@unique
class Gender(Enum):
    '''
    MALE: 男
    FEMALE: 女
    NONE: 未知
    '''
    MALE = 1
    FEMALE = 0
    NONE = 2
