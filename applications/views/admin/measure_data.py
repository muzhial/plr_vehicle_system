from flask import Blueprint, render_template, request, jsonify

from applications.models.admin_measure_data import MeasureData
from applications.service.admin.data_proc import (
    get_measure_data, save_measure_data, update_measure_data,
    delete_data_by_id, bulk_save_measure_data)
from applications.service.common.response import (
        table_api, success_api, fail_api, res_api)
from applications.service.route_auth import authorize_and_log

admin_measure_data = Blueprint(
    'adminMeasure', __name__, url_prefix='/admin/measure')


@admin_measure_data.route('/data')
@authorize_and_log("admin:measure:main")
def dictCode_data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    data, count = get_measure_data(page=page, limit=limit)
    return table_api(data=data,count=count)


# @admin_measure_data.route('/save', methods=['POST'])
# @authorize_and_log("admin:measure:add")
# def dictData_save():
#     req_json = request.json
#     res = save_measure_data(req_json=req_json)
#     if res == None:
#         return res_api(success=False,
#                        msg="add measure data fail",
#                        status=True)
#     return res_api(success=True,
#                    msg="add measure data success")


@admin_measure_data.route('/save', methods=['POST'])
@authorize_and_log("admin:measure:add")
def dictData_save():
    req_json = request.json
    # res = save_measure_data(req_json=req_json)
    res = bulk_save_measure_data(req_json=req_json)
    if res == None:
        return res_api(success=False,
                       msg="add measure data fail",
                       status=True)
    return res_api(success=True,
                   msg="add measure data success")


@admin_measure_data.route('/update', methods=['PUT'])
@authorize_and_log("admin:measure:edit")
def dictData_update():
    req_json = request.json
    update_measure_data(req_json)
    return res_api(
        success=True,
        msg="update measure data success",
        status=True)


@admin_measure_data.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:measure:remove")
def dictData_delete(id):
    res = delete_data_by_id(id)
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")
