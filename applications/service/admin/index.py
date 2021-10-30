from io import BytesIO
from flask import session, make_response
from flask_login import current_user
from applications.models.admin_power import PowerSchema


# 授权路由存入 session
def add_auth_session():
    role = current_user.role
    user_power = []
    for i in role:
        if i.enable == 0:
            continue
        for p in i.power:
            if p.enable == 0:
                continue
            user_power.append(p.code)
    session['permissions'] = user_power

