from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required

from applications.service.admin.role import (
    get_role_data_dict, add_role, get_role_power, update_role_power, \
    get_role_by_id, update_role, remove_role, batch_remove, enable_status, \
    disable_status)
from applications.service.common.response import (
    table_api, success_api, fail_api, res_api)
from applications.service.route_auth import authorize_and_log

admin_role = Blueprint('adminRole', __name__, url_prefix='/admin/role')


# 表格数据
@admin_role.route('/data')
@authorize_and_log("admin:role:main")
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    roleName = request.args.get('roleName', type=str)
    roleCode = request.args.get('roleCode', type=str)
    filters = {}
    if roleName:
        filters["name"] = ('%' + roleName + '%')
    if roleCode:
        filters["code"] = ('%' + roleCode + '%')
    data, count = get_role_data_dict(page=page, limit=limit, filters=filters)
    return table_api(data=data, count=count)


# 角色增加
@admin_role.route('/save', methods=['POST'])
@authorize_and_log("admin:role:add")
def save():
    req = request.json
    add_role(req=req)
    return res_api(
        msg="add role success",
        success=True)


# 获取角色权限
@admin_role.route('/getRolePower/<int:id>')
@authorize_and_log("admin:role:main")
def getRolePower(id):
    powers = get_role_power(id)
    return res_api(
        msg='get role power success',
        success=True,
        data=powers)


# 保存角色权限
@admin_role.route('/saveRolePower', methods=['PUT'])
@authorize_and_log("admin:role:edit")
def saveRolePower():
    req_form = request.json
    powerIds = req_form.get("powerIds")
    power_list = powerIds.split(',')
    roleId = req_form.get("roleId")
    update_role_power(id=roleId, power_list=power_list)
    return res_api(
        msg="auth role power success",
        success=True)


# 更新角色
@admin_role.route('/update', methods=['PUT'])
@authorize_and_log("admin:role:edit")
def update():
    res = update_role(request.json)
    if not res:
        return res_api(
            msg="update role fail",
            success=False)
    return res_api(
        msg="update role success",
        success=True)


# enable role
@admin_role.route('/enable', methods=['PUT'])
@authorize_and_log("admin:role:edit")
def enable():
    id = request.json.get('roleId')
    print(id)
    if id:
        res = enable_status(id)
        if not res:
            return res_api(
                msg="enable role fail",
                success=False)
        return res_api(
            msg="enable role success",
            success=True)
    return res_api(
        msg="data error",
        success=False)


# disable role
@admin_role.route('/disable', methods=['PUT'])
@authorize_and_log("admin:role:edit")
def disenable():
    id = request.json.get('roleId')
    if id:
        res = disable_status(id)
        if not res:
            return res_api(
                msg="disable role fail")
        return res_api(
            msg="disable role success",
            success=True)
    return res_api(
        msg="data error",
        success=False)


# 角色删除
@admin_role.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:role:remove")
def remove(id):
    res = remove_role(id)
    if not res:
        return res_api(
            msg="del role fail",
            success=False)
    return res_api(
        msg="del role success",
        success=True)


# 批量删除
@admin_role.route('/batchRemove', methods=['DELETE'])
@authorize_and_log("admin:role:remove")
@login_required
def batchRemove():
    ids = request.form.getlist('ids[]')
    batch_remove(ids)
    return res_api(
        msg="batch remove success",
        success=True)

