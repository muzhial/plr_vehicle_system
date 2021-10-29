from flask import (
    Blueprint, render_template, jsonify, request, session, redirect, url_for)
from flask_login import login_user, login_required, logout_user, current_user
from applications.service.admin.index import (
    add_auth_session, make_menu_tree, get_captcha)
from applications.service.admin_log import login_log
from applications.models.admin_user import User
from applications.service.common.response import fail_api, success_api

admin_index = Blueprint('adminIndex', __name__, url_prefix='/admin')


#  @admin_index.route('/')
#  @login_required
#  def index():
    #  user = current_user
    #  return render_template('admin/index.html', user=user)


# 获取验证码
# @admin_index.route('/getCaptcha', methods=["GET"])
# def getCaptcha():
#     resp,code=get_captcha()
#     session["code"] = code
#     return resp


# login
@admin_index.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req = request.form
        username = req.get('username')
        password = req.get('password')
        # code = req.get('captcha')

        if not username or not password or not code:
            return fail_api(msg="User name or password not input")
        # s_code = session.get("code", None)

        # if not all([code, s_code]):
        #     return fail_api(msg="参数错误")
        # if code != s_code:
        #     return fail_api(msg="验证码错误")

        user = User.query.filter_by(username=username).first()

        if user is None:
            return fail_api(msg="User not exists")

        if user.enable is 0:
            return fail_api(msg="User not enabled")

        if username == user.username and user.validate_password(password):
            login_user(user)
            # write login log doc
            login_log(request, uid=user.id, is_access=True)
            add_auth_session()
            return success_api(msg="Login success")
        login_log(request, uid=user.id, is_access=False)
        return fail_api(msg="username or password not correctly")
    if current_user.is_authenticated:
        return redirect(url_for('adminIndex.index'))
    return render_template('admin/login.html')


# logout
@admin_index.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return success_api(msg="Logout success")


# 菜单
@admin_index.route('/menu')
@login_required
def menu():
    menu_tree = make_menu_tree()
    return jsonify(menu_tree)


# 控制台页面
@admin_index.route('/welcome')
@login_required
def welcome():
    return render_template('admin/console/console.html')

