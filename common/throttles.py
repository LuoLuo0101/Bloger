# -*- coding: utf-8 -*-
# @Time    : 18-1-16 下午7:44
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : throttles.py
# @Software: PyCharm

from rest_framework.throttling import AnonRateThrottle


class NormalAnonRateThrottle(AnonRateThrottle):
    scope = 'normal_anon'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return None

        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }
