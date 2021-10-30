from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from applications.models.admin_user import User
from applications.models.admin_role import Role
from applications.service.admin.user import (
    get_user_data_dict, add_user, delete_by_id,
    batch_remove, update_user, update_user_role,
    is_user_exists, add_user_role, enable_status, disable_status,
    edit_password, get_current_user_logs, update_current_user_info,
    update_avatar)
from applications.service.common.response import (
    table_api, fail_api, success_api, res_api)
from applications.service.route_auth import authorize_and_log

admin_user = Blueprint('adminUser', __name__, url_prefix='/admin/user')


# user find by page api
@admin_user.route('/data')
@authorize_and_log("admin:user:main")
def data():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    realName = request.args.get('realName', type=str)
    username = request.args.get('username', type=str)
    filters = {}
    if realName:
        filters["realname"] = ('%' + realName + '%')
    if username:
        filters["username"] = ('%' + username + '%')
    user_data, count = get_user_data_dict(
        page=page, limit=limit, filters=filters)
    return table_api(data=user_data, count=count)


@admin_user.route('/save', methods=['POST'])
@authorize_and_log("admin:user:add")
def save():
    req_json = request.json
    a = req_json.get("roleIds")
    username = req_json.get('username')
    realName = req_json.get('realName')
    password = req_json.get('password')
    role_ids = a.split(',')

    if not username or not realName or not password:
        return res_api(
            msg="username and password not allow empty",
            status=False)

    if is_user_exists(username):
        return res_api(msg="user already exists", status=False)

    id = add_user(username, realName, password)
    add_user_role(id, role_ids)

    return res_api(msg="add user success", status=True)


# delete user api
@admin_user.route('/remove/<int:id>', methods=['DELETE'])
@authorize_and_log("admin:user:remove")
def delete(id):
    res = delete_by_id(id)
    if not res:
        return fail_api(msg="delete user failed")
    return success_api(msg="delete user success")


# edit user
@admin_user.route('/update', methods=['PUT'])
@authorize_and_log("admin:user:edit")
def update():
    req_json = request.json
    a = req_json.get("roleIds")
    id = req_json.get("userId")
    username = req_json.get('username')
    realName = req_json.get('realName')
    role_ids = a.split(',')
    update_user(id, username, realName)
    update_user_role(id, role_ids)
    return success_api(msg="update user success")


# alter current user info: realName and details
@admin_user.route('/updateInfo', methods=['PUT'])
@login_required
def updateInfo():
    res_json = request.json
    if not update_current_user_info(req_json=res_json):
        return fail_api(msg="error")
    return success_api(msg="Update success")


# change current user password
@admin_user.route('/editPassword', methods=['PUT'])
@login_required
def edit_password_put():
    res_json = request.json
    return edit_password(res_json=res_json)


# enable user
@admin_user.route('/enable', methods=['PUT'])
@authorize_and_log("admin:user:edit")
def enable():
    id = request.json.get('userId')
    print(id)
    if id:
        res = enable_status(id)
        if not res:
            return res_api(
                msg="enable user error",
                success=False)
        return res_api(
            msg="enable user success",
            success=True)
    return res_api(
        msg="data error",
        success=False)


# unable user
@admin_user.route('/disable', methods=['PUT'])
@authorize_and_log("admin:user:edit")
def disenable():
    id = request.json.get('userId')
    if id:
        res = disable_status(id)
        if not res:
            return res_api(
                msg="disable user error",
                success=False)
        return res_api(
            msg="unable success",
            success=True)
    return res_api(
        msg="data error",
        success=False)


# batch del
@admin_user.route('/batchRemove', methods=['DELETE'])
@authorize_and_log("admin:user:remove")
def batchRemove():
    ids = request.form.getlist('ids[]')
    batch_remove(ids)
    return res_api(
        msg="batch del success",
        success=True)

