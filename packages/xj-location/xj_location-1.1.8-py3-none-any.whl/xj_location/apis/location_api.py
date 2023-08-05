# encoding: utf-8
"""
@project: djangoModel->location_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 定位接口
@created_time: 2022/9/7 13:27
"""

# ================ 定位操作 =====================
from rest_framework.views import APIView

from ..services.location_service import LocationService
from ..utils.custom_response import util_response
from ..utils.custom_tool import *
from ..utils.join_list import JoinList


class LocationAPI(APIView):

    @request_params_wrapper
    def list(self, *args, request_params, **kwargs):
        """
        用户组 列表接口
        :param request_params: 解析的请求参数
        :return: response
        """
        # ================== section 信息id列表反查询 start===============================
        thread_params = format_params_handle(
            param_dict=request_params,
            filter_filed_list=["title", "subtitle", "access_level", "author"],
            is_remove_empty=True
        )
        if thread_params:
            try:
                if not getattr(sys.modules.get("xj_thread.services.thread_list_service"), "ThreadListService", None):
                    from xj_thread.services.thread_list_service import ThreadListService
                else:
                    ThreadListService = getattr(sys.modules.get("xj_thread.services.thread_list_service"), "ThreadListService")
                thread_ids, err = ThreadListService.search_ids(search_prams=thread_params)
                request_params.setdefault("thread_id_list", thread_ids)
            except Exception as e:
                write_to_log(prefix="查询定位列表异常", err_obj=e, content="thread_params:" + str(thread_params))
        # ================== section 信息id列表反查询 end  ===============================

        # 获取定位信息
        filter_fields = request_params.pop("filter_fields", None)
        data, err = LocationService.location_list(request_params, filter_fields=filter_fields)
        if err:
            return util_response(err=1000, msg=err)

        # ================== section 拼接信息表信息 start  ===============================
        need_thread, is_pass = force_transform_type(variable=request_params.pop("need_thread", None), var_type="bool", default=False)
        ThreadListService, import_err = dynamic_load_class(import_path="xj_thread.services.thread_list_service", class_name="ThreadListService")
        thread_id_list = list(set([i["thread_id"] for i in data["list"] if i.get("thread_id")]))
        if thread_id_list and need_thread and not import_err:
            try:
                remove_fields = "!!!create_time;update_time;content"  # note 存在字段冲突,去掉冲突的字段
                thread_infos, err = ThreadListService.search(id_list=thread_id_list, filter_fields=remove_fields)
                data["list"] = JoinList(l_list=data["list"], r_list=thread_infos, l_key="thread_id", r_key='id').join()
            except Exception as e:
                write_to_log(prefix="定位查询拼接thread模块信息异常", err_obj=e, content="thread_id_list:" + str(thread_id_list))
        # ================== section 拼接信息表信息 end    ===============================
        return util_response(data=data)

    @request_params_wrapper
    def put(self, *args, request_params, **kwargs):
        """定位编辑"""
        request_params.setdefault("id", kwargs.get("id", None))
        data, err = LocationService.edit_location(request_params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    @request_params_wrapper
    def post(self, *args, request_params, **kwargs):
        """定位添加"""
        # ============ section 信息表添加  start ============
        # 如果参数中存在一下的参数就会触发添加信息模块的信息
        must_thread_params = format_params_handle(
            param_dict=request_params,
            filter_filed_list=["category_id", "title", "subtitle", "summary"]
        )
        ThreadItemService, import_err = dynamic_load_class(import_path="xj_thread.services.thread_item_service", class_name="ThreadItemService")
        if not import_err and must_thread_params:
            request_params["has_enroll"] = 1  # 默认参数开启报名
            if not request_params.get("thread_id"):
                data, err = ThreadItemService.add(request_params)
            else:
                data, err = ThreadItemService.edit(request_params, request_params.get("thread_id"))
            if err:
                return util_response(err=1002, msg="联动信息添加错误：" + err)
            request_params.setdefault("thread_id", data.get("id", 0))
        # ============ section 信息表添加  end   ============

        # ======== section 定位添加 start ==============
        data, err = LocationService.add_location(request_params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
        # ======== section 定位添加 end   ==============

    def delete(self, request, **kwargs):
        # 用户组 删除接口
        id = parse_data(request).get("id", None) or kwargs.get("id")
        if not id:
            return util_response(err=1000, msg="id 必传")
        data, err = LocationService.del_location(id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    def test(self):
        # 测试接口
        params = {"thread_id_list": [1, 2]}
        data, err = LocationService.location_list(params, False)
        return util_response(data=data)
