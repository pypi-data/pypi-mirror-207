from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from xj_user.services.user_detail_info_service import DetailInfoService
from xj_user.utils.user_wrapper import user_authentication_force_wrapper
from ..models import Enroll
from ..service.enroll_record_serivce import EnrollRecordServices
from ..service.valuation_service import ValuationService
from ..utils.custom_response import util_response
from ..utils.custom_tool import parse_data, flow_service_wrapper, write_to_log, force_transform_type
from ..utils.custom_tool import request_params_wrapper
from ..utils.join_list import JoinList


class RecordAPI(APIView):
    # 添加记录,用户报名
    @api_view(['POST'])
    @user_authentication_force_wrapper
    @request_params_wrapper
    @flow_service_wrapper
    def add(self, *args, user_info=None, request_params=None, **kwargs, ):
        # 提取参数
        request_params, is_pass = force_transform_type(variable=request_params, var_type="dict", default={})
        enroll_id, is_pass = force_transform_type(variable=request_params.get("enroll_id"), var_type="int")
        # 检查报名ID是否正确
        if not enroll_id:
            return util_response(err=1000, msg="没有找到有效的报名ID")
        enroll_info = Enroll.objects.filter(id=enroll_id).first()
        if not enroll_info:
            return util_response(err=1001, msg="报名ID不正确")
        # 用户ID判断，不允许匿名报名，但是可以代报名（指派）。
        request_params.setdefault("user_id", user_info.get("user_id", None))
        if not request_params.get("user_id"):
            return util_response(err=1006, msg="没有找到有效的用户ID")
        # 入库之前进行计价
        try:
            request_params.setdefault("again_price", 0)
            valuation_res, err = ValuationService.valuate(
                enroll_rule_group_id=enroll_info.enroll_rule_group_id or 1,
                variables_dict=request_params
            )
            # TODO 这里如果业务变动还是需要改代码，优化到动态处理并放在参数里面
            request_params["initiator_again_price"] = valuation_res.get("initiator_again_price", 0)
            write_to_log(prefix="报名记录添加，计价结果", content="enroll_info:" + str(enroll_info) + "valuation_res:" + str(valuation_res))
        except Exception as e:
            write_to_log(prefix="报名记录添加触发计价错误", err_obj=e)
        # 添加数据
        data, err = EnrollRecordServices.record_add(request_params)
        if err:
            return util_response(err=1002, msg=err)
        return util_response(data={"id": data.get("id")})

    @require_http_methods(['GET'])
    def list(self, *args, **kwargs, ):
        params = parse_data(self)
        need_pagination, is_pass = force_transform_type(variable=params.get("need_pagination", 1), var_type="bool", default=True)
        data, err = EnrollRecordServices.record_list(params=params, need_pagination=need_pagination)
        if err:
            return util_response(err=1000, msg=err)
        user_ids = []
        if need_pagination:
            user_infos = DetailInfoService.get_list_detail({}, user_ids)
            data["list"] = JoinList(data["list"], user_infos, "user_id", "user_id").join()
        else:
            user_infos = DetailInfoService.get_list_detail({}, user_ids)
            data = JoinList(data, user_infos, "user_id", "user_id").join()

        return util_response(data=data)

    @require_http_methods(['GET'])
    def list_v2(self, *args, **kwargs, ):
        params = parse_data(self)
        data, err = EnrollRecordServices.complex_record_list(params=params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    @api_view(['DELETE'])
    def record_del(self, *args, **kwargs, ):
        params = parse_data(self) or {}
        pk = kwargs.get("pk") or params.pop("id")
        data, err = EnrollRecordServices.record_del(pk)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    @api_view(['PUT'])
    @user_authentication_force_wrapper
    @request_params_wrapper
    @flow_service_wrapper
    def record_edit(self, *args, request_params, **kwargs, ):
        pk = kwargs.get("pk") or request_params.pop("id")
        # 检查报名记录是否可以修改为草稿,防止用户指派完成后，镖师取消报名
        # is_can_cancel, err = EnrollRecordServices.check_can_cancel(pk, change_code=request_params.get("enroll_status_code"))
        # if not is_can_cancel:
        #     return util_response()

        data, err = EnrollRecordServices.record_edit(request_params, pk)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    @require_http_methods(['GET'])
    def record_detail(self, *args, **kwargs, ):
        params = parse_data(self) or {}
        pk = kwargs.get("pk", None) or params.pop("id", None) or params.pop("record_id", None) or None
        if not pk:
            return util_response(err=1000, msg="参数错误")
        data, err = EnrollRecordServices.record_detail(pk, search_params=params)

        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    @api_view(['GET'])
    @user_authentication_force_wrapper
    @request_params_wrapper
    @flow_service_wrapper
    def appoint(self, *args, user_info=None, **kwargs, ):
        """
        需求描述：报名可多人报名，不在自动成单，可以手动指派报名
        1.由用户或者客服进行指派工作人员完成任务。
        2.没有被选中的用户，报名状态修改成草稿状态。
        3.主报名项目，则进入代补差价状态。
        :return: response
        """
        params = parse_data(self)
        enroll_id = params.get("enroll_id", None)
        record_id = params.get("record_id", None)
        subitem_id = params.get("subitem_id", None)
        if enroll_id is None or record_id is None or subitem_id is None:
            return util_response(err=1000, msg="参数错误")
        data, err = EnrollRecordServices.appoint(enroll_id, record_id, subitem_id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data, msg="指派成功")

    @api_view(['GET'])
    @user_authentication_force_wrapper
    @request_params_wrapper
    @flow_service_wrapper
    def old_appoint(self, *args, user_info=None, **kwargs, ):
        """
        需求描述：报名可多人报名，不在自动成单，可以手动指派报名
        1.由用户或者客服进行指派工作人员完成任务。
        2.没有被选中的用户，报名状态修改成草稿状态。
        3.主报名项目，则进入代补差价状态。
        :return: response
        """
        params = parse_data(self)
        enroll_id = params.get("enroll_id", None)
        record_id = params.get("record_id", None)
        subitem_id = params.get("subitem_id", None)
        if enroll_id is None or record_id is None or subitem_id is None:
            return util_response(err=1000, msg="参数错误")
        data, err = EnrollRecordServices.old_appoint(enroll_id, record_id, subitem_id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data, msg="指派成功")
