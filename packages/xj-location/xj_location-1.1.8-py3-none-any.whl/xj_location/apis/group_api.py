# encoding: utf-8
"""
@project: djangoModel->group_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/9/7 15:05
"""
from rest_framework.views import APIView

from ..services.location_group_services import LocationGroupService
from ..utils.custom_response import util_response
from ..utils.custom_tool import request_params_wrapper


# 临时接口
class GroupApi(APIView):

    @request_params_wrapper
    def get(self, *args, request_params, **kwargs):
        data, err = LocationGroupService.group_list(params=request_params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
