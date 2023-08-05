# encoding: utf-8
"""
@project: djangoModel->location_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 定位服务
@created_time: 2022/9/7 13:38
"""
from django.core.paginator import Paginator, EmptyPage

from ..models import Location
from ..utils.custom_tool import force_transform_type, filter_fields_handler, format_params_handle, filter_result_field


class LocationService:
    location_all_fields = [i.name for i in Location._meta.fields]

    @staticmethod
    def location_list(params: dict = None, need_pagination: bool = True, filter_fields: "list|str" = None, result_prefix: str = None, **kwargs):
        """
        定位列表接口
        :param result_prefix: 返回结字段添加前缀
        :param params: 搜索参数,仅仅在不分页（服务层调用的时候）生效
        :param need_pagination: 是否需要分页
        :param fields: 过滤返回字段
        :return: data,err
        """
        # ============== section 过滤字段处理 start =======================
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        page, is_pass = force_transform_type(variable=params.pop("page", 1), var_type="int", default=1)
        size, is_pass = force_transform_type(variable=params.pop("size", 10), var_type="int", default=10)
        need_pagination, is_pass = force_transform_type(variable=need_pagination, var_type="bool", default=True)
        filter_fields = filter_fields_handler(
            input_field_expression=filter_fields,
            default_field_list=["name", "thread_id", "region_code", "longitude", "latitude", "altitude", "coordinate_type", "created_time"],
            all_field_list=LocationService.location_all_fields
        )
        filter_fields = list(set(filter_fields + ["thread_id"]))  # 强制返回字段, 存在其他模块强依赖关系所以强制返回
        # 搜索参数校验
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "id|int", "location_id|int", "region_code|int", "name", "user_id|int", "by_user_id|int", "group_id|int", "coordinate_type|int",
                # 列表搜索
                "user_id_list|list", "user_id_ban_list|list", "location_id_list|list", "id_list|list", "thread_id_list|list",
                # 支持经纬度海拔搜索，矩阵范围搜索
                "longitude_min|float", "longitude_max|float", "latitude_min|float", "latitude_max|float", "altitude_min|float", "altitude_max|float",
                # 时间范围搜索
                "created_time_start", "created_time_end"
            ],
            alias_dict={
                "name": "name__contains", "location_id": "id",
                "user_id_list": "user_id__in", "location_id_list": "id__in", "id_list": "id__in", "thread_id_list": "thread_id__in",
                "longitude_min": "longitude__gte", "longitude_max": "longitude__lte", "latitude_min": "latitude__gte", "latitude_max": "latitude__lte",
                "altitude_min": "altitude__gte", "altitude_max": "altitude__lte",
                "created_time_start": "created_time__gte", "created_time_end": "created_time__lte"
            },
        )
        user_id_ban_list = params.pop("user_id_ban_list", None)
        # ============== section 过滤字段处理 end    =======================

        # 构建ORM
        location_obj = Location.objects.values(*filter_fields)
        location_obj = location_obj.filter(**params)
        if user_id_ban_list:
            location_obj = location_obj.exclude(user_id__in=location_obj)

        # 分情况查询
        total = location_obj.count()
        if not need_pagination and total <= 2000:  # 支持其他服务调用,不需要分页查询,但是限制限制上限条数
            finish_list = list(location_obj)
            # note 其他模块调用该服务时候，存在字段冲突可使用need_prefix，添加自定义前缀。
            if not result_prefix is None and isinstance(finish_list, list) and len(finish_list) >= 1 and isinstance(finish_list[0], dict):
                result_prefix, is_pass = force_transform_type(variable=result_prefix, var_type="str", default="location")
                finish_list = filter_result_field(
                    result_list=finish_list,
                    alias_dict={k: result_prefix + "_" + k for k in finish_list[0].keys()}
                )
            return finish_list, None
        else:  # 正常分页查询
            paginator = Paginator(location_obj, size)
            try:
                finish_set = paginator.page(page)
            except EmptyPage:
                finish_set = paginator.page(paginator.num_pages)
            # 如果其他模块调用时候存在字段冲突，可只用该参数，吧所有的参数添加前缀
            finish_list = list(finish_set.object_list)
            return {"page": page, "size": size, "total": total, "list": finish_list}, None

    @staticmethod
    def add_location(params):
        try:
            params = format_params_handle(
                param_dict=params,
                is_validate_type=True,
                filter_filed_list=[
                    "region_code|int", "name", "address", "coordinate_type|int", "longitude|float", "latitude|float",
                    "altitude|float", "user_id|int", "by_user_id|int", "group_id|int", "created_time|date", "thread_id|int", "category_id|int"
                ]
            )
        except ValueError as e:
            return None, str(e)
        if not params:
            return None, "参数不能为空"
        instance = Location.objects.create(**params)
        return {"id": instance.id}, None

    @staticmethod
    def edit_location(params):
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "id", "region_code", "name", "address", "coordinate_type", "longitude",
                "latitude", "altitude", "user_id", "by_user_id", "group_id", "created_time",
                "category_id", "classify_id"
            ]
        )
        id = params.pop("id", None)
        if not id:
            return None, "ID 不可以为空"
        if not params:
            return None, "没有可以修改的字段"
        instance = Location.objects.filter(id=id)
        if params:
            instance.update(**params)
        return None, None

    @staticmethod
    def del_location(id):
        if not id:
            return None, "ID 不可以为空"
        instance = Location.objects.filter(id=id)
        if instance:
            instance.delete()
        return None, None
