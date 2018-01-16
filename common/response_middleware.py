# -*- coding: utf-8 -*-
# @Time    : 18-1-16 下午6:05
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : response_middleware.py
# @Software: PyCharm
import json

from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.response import Response

from common.message_helper import genernal_message


class OutputMiddleWare(MiddlewareMixin):

    def process_response(self, request, response):
        print(type(response))
        code = response.status_code
        if (isinstance(response, Response) or isinstance(response, JsonResponse) or isinstance(response, HttpResponse)) \
                and response.data and isinstance(response.data, dict):
            result = response.data
            if result.get("code", None) is None or result.get("data", None) is None or (
                    not isinstance(result.get("data", None), dict)):
                result = genernal_message(code=code, msg="success" if code < status.HTTP_400_BAD_REQUEST else "failed",
                                          data=result)
                response.data = result
                response.content = json.dumps(result)
        return response
