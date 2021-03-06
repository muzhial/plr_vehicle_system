from functools import wraps
from flask import abort, request, jsonify, session
from flask_login import login_required
from applications.service.admin_log import admin_log
from applications.service.common.response import res_api


def authorize(power: str):
    def decorator(func):
        @login_required
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not power in session.get('permissions'):
                if request.method == 'GET':
                    abort(403)
                else:
                    return res_api(
                        success=False,
                        msg="insufficient privileges")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def authorize_and_log(power: str):
    def decorator(func):
        @login_required
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not power in session['permissions']:
                admin_log(request=request, is_access=False)
                if request.method == 'GET':
                    abort(403)
                else:
                    return res_api(
                        success==False,
                        msg="insufficient privileges")
            admin_log(request=request, is_access=True)
            return func(*args, **kwargs)

        return wrapper

    return decorator

