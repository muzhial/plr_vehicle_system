import datetime

from applications.models import db, ma
from marshmallow import fields


class Photo(db.Model):
    __tablename__ = 'admin_photo'
    id = db.Column(db.Integer, primary_key=True)
    measure_data_id = db.Column(db.Integer)
    name = db.Column(db.String(255), nullable=False)
    href = db.Column(db.String(255))
    mime = db.Column(db.CHAR(50), nullable=True)
    size = db.Column(db.CHAR(30), nullable=True)
    shape = db.Column(db.CHAR(50), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime,
                            default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)


class PhotoSchema(ma.Schema):
    id = fields.Integer(attribute='id')
    measureDataId = fields.Integer(attribute='measure_data_id')
    name = fields.Str(attribute='name')
    href = fields.Str(attribute='href')
    mime = fields.Str(attribute='mime')
    size = fields.Str(attribute='size')
    shape = fields.Str(attribute='shape')
    createTime = fields.DateTime(attribute='create_time')
    updateTime = fields.DateTime(attribute='update_time')


class DetectionData(db.Model):
    __tablename__ = 'admin_detection_data'

    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer)
    result_str = db.Column(db.String(512))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)


class DetectionDataSchema(ma.Schema):
    id = fields.Integer(attribute='id')
    photoId = fields.Integer(attribute='photo_id')
    resultStr = fields.Str(attribute='result_str')
    createTime = fields.DateTime(attribute='create_time')

