from flask import Blueprint, render_template, request, jsonify
from applications.service.admin.power import (
    get_power_dict, select_parent, save_power, remove_power, get_power_by_id, \
    update_power, enable_status, disable_status, batch_remove)
from applications.service.common.response import success_api, fail_api, res_api
from applications.service.route_auth import authorize_and_log

admin_power = Blueprint('adminPower', __name__, url_prefix='/admin/power')


@admin_power.route('/data')
@authorize_and_log("admin:power:main")
def data():
    power_data = get_power_dict()
    return res_api(
        msg='get power data success',
        success=True,
        data=power_data)


# @admin_power.route('/selectParent')
# @authorize_and_log("admin:power:main")
# def selectParent():
    # power_data = select_parent()
    # res = {
        # "status": {"code": 200, "message": "默认"},
        # "data": power_data

    # }
    # return jsonify(res)


@admin_power.route('/save', methods=['POST'])
@authorize_and_log("admin:power:add")
def save():
    req = request.json
    save_power(req)
    return res_api(
        msg="add power success",
        success=True)


@admin_power.route('/update', methods=['PUT'])
@authorize_and_log("admin:power:edit")
def update():
    res = update_power(request.json)
    if not res:
        return res_api(
            msg="update power privilege fail",
            success=False)
    return res_api(
        msg="update power privilege success",
        success=True)


@admin_power.route('/enable', methods=['PUT'])
@authorize_and_log("admin:power:edit")
def enable():
    id = request.json.get('powerId')
    print(id)
    if id:
        res = enable_status(id)
        if not res:
            return res_api(
                msg="enable power fail",
                success=False)
        return res_api(
            msg="enable power success",
            success=True)
    return res_api(
        msg="data error",
        success=False)


@admin_power.route('/disable', methods=['PUT'])
@authorize_and_log("admin:power:edit")
def disenable():
    id = request.json.get('powerId')
    print(id)
    if id:
        res = disable_status(id)
        if not res:
            return res_api(
                msg="disable power fail",
                success=False)
        return res_api(
            msg="disable power success",
            success=True)
    return res_api(
        msg="data error",
        success=False)


@admin_power.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:power:remove")
def remove(id):
    r = remove_power(id)
    if r:
        return res_api(
            msg="del power success",
            success=True)
    else:
        return res_api(
            msg="del power fail",
            success=False)


# 批量删除
@admin_power.route('/batchRemove', methods=['DELETE'])
@authorize_and_log("admin:power:remove")
def batchRemove():
    ids = request.form.getlist('ids[]')
    batch_remove(ids)
    return res_api(
        msg="batch del power success",
        success=True)

