from flask import (
    Blueprint, render_template, jsonify, request, session, redirect, url_for)
from flask_login import login_user, login_required, logout_user, current_user
from applications.service.admin.index import add_auth_session
from applications.service.admin_log import login_log
from applications.models.admin_user import User
from applications.service.common.response import (
    fail_api, success_api, res_api)

admin_index = Blueprint('adminIndex', __name__, url_prefix='/admin')


# login
@admin_index.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req = request.form
        username = req.get('username')
        password = req.get('password')

        if not username or not password:
            return fail_api(msg="user name or password not input")

        user = User.query.filter_by(username=username).first()

        if user is None:
            return fail_api(msg="user not exists")

        if user.enable == 0:
            return fail_api(msg="user not enabled")

        if username == user.username and user.validate_password(password):
            login_user(user)
            # write login log doc
            login_log(request, uid=user.id, is_access=True)
            add_auth_session()
            return res_api(msg='login success', status=True)
        login_log(request, uid=user.id, is_access=False)
        return res_api(
            msg="username or password not correctly",
            status=False)
    else:
        return res_api(msg='/login support POST', status=False)


# logout
@admin_index.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return res_api(msg="logout success", status=True)

