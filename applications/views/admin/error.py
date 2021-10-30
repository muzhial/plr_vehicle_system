from flask import render_template

from applications.service.common.response import res_api


def init_error(app):

    @app.errorhandler(403)
    def page_not_found(e):
        # return render_template('errors/403.html'), 403
        return res_api(
            msg='403 error',
            success=False,
            status=False)

    @app.errorhandler(404)
    def page_not_found(e):
        # return render_template('errors/404.html'), 404
        return res_api(
            msg='404 error',
            success=False,
            status=False)

    @app.errorhandler(500)
    def internal_server_error(e):
        # return render_template('errors/500.html'), 500
        return res_api(
            msg='500 error',
            success=False,
            status=False)

