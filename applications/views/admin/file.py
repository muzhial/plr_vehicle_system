import os
from flask import Blueprint, request, render_template, jsonify, current_app
from applications.models import db
from applications.models.admin_photo import Photo
from applications.service.admin.file import (
    get_photo, upload_one, delete_photo_by_id)
from applications.service.common.response import (
    table_api, success_api, fail_api, res_api)
from applications.service.route_auth import authorize_and_log


admin_file = Blueprint('adminFile', __name__, url_prefix='/admin/file')


@admin_file.route('/data')
@authorize_and_log("admin:file:main")
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    data, count = get_photo(page=page, limit=limit)
    return table_api(data=data, count=count)


@admin_file.route('/upload', methods=['GET', 'POST'])
@authorize_and_log("admin:file:add")
def upload():
    if request.method == 'POST' and 'file' in request.files:
        photo = request.files['file']
        mime = request.files['file'].content_type
        file_url = upload_one(photo=photo, mime=mime)
        return res_api(msg='upload file success',
                       success=True,
                       data={'src': file_url})

    return res_api(msg='supported methods: [POST]',
                   success=False)


@admin_file.route('/delete', methods=['GET', 'POST'])
@authorize_and_log("admin:file:delete")
def delete():
    id = request.form.get('id')
    res = delete_photo_by_id(id)
    if res:
        return res_api(msg="delete file success",
                       success=True)
    else:
        return res_api(msg="delete file fail",
                       success=False)


@admin_file.route('/batchRemove', methods=['GET', 'POST'])
@authorize_and_log("admin:file:delete")
def batchRemove():
    ids = request.form.getlist('ids[]')
    photo_name = Photo.query.filter(Photo.id.in_(ids)).all()
    upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
    for p in photo_name:
        os.remove(upload_url + '/' + p.name)
    photo = Photo.query.filter(
            Photo.id.in_(ids)
        ).delete(synchronize_session=False)
    db.session.commit()
    if photo:
        return res_api(msg="batch delete file success",
                       success=True)
    else:
        return res_api(msg="batch delete file fail",
                       success=False)
