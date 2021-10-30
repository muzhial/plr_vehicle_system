from applications.views.admin.index import admin_index
from applications.views.admin.user import admin_user
from applications.views.admin.file import admin_file
from applications.views.admin.admin_log import admin_log
from applications.views.admin.power import admin_power
from applications.views.admin.role import admin_role
from applications.views.admin.measure_data import admin_measure_data


def init_adminViews(app):
    """
    init blueprint
    """
    app.register_blueprint(admin_index)
    app.register_blueprint(admin_user)
    app.register_blueprint(admin_file)
    app.register_blueprint(admin_log)
    app.register_blueprint(admin_power)
    app.register_blueprint(admin_role)
    app.register_blueprint(admin_measure_data)

