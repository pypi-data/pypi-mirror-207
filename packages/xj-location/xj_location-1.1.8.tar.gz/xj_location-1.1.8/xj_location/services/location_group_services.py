# encoding: utf-8
"""
@project: djangoModel->location_group_services
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 定位分组
@created_time: 2023/5/6 9:59
"""
from django.core.paginator import Paginator, EmptyPage

from xj_location.models import LocationGroup
from ..utils.custom_tool import format_params_handle, force_transform_type


class LocationGroupService():
    @staticmethod
    def group_list(params: dict = None, filter_fields: "list|str" = None):
        # 参数处理
        page, is_pass = force_transform_type(variable=params.pop("page", 1), var_type="int", default=1)
        size, is_pass = force_transform_type(variable=params.pop("size", 10), var_type="int", default=10)
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["id|int", "group_name", "id_list"],
            alias_dict={"group_name": "group_name__contains", "id_list": "id__in"},
        )
        # 构建ORM
        location_group_obj = LocationGroup.objects.filter(**params).values(*filter_fields)
        total = location_group_obj.count()

        # 分页查询
        paginator = Paginator(location_group_obj, size)
        try:
            finish_set = paginator.page(page)
        except EmptyPage:
            finish_set = paginator.page(paginator.num_pages)

        return {"page": page, "size": size, "total": total, "list": list(finish_set.object_list)}, None
