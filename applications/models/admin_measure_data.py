import datetime

from applications.models import db, ma
from marshmallow import fields


class MeasureData(db.Model):
    __tablename__ = 'admin_measure_data'

    id = db.Column(db.Integer, primary_key=True)
    coord_xyz = db.Column(db.String(255))
    measure_address = db.Column(db.String(255))
    measure_time = db.Column(db.DateTime)
    measure_status = db.Column(db.Integer)
    measure_info = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime,
                            default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)


class MeasureDataSchema(ma.Schema):
    dataId = fields.Integer(attribute='id')
    coordXYZ = fields.Str(attribute='coord_xyz')
    measureAddress = fields.Str(attribute='measure_address')
    measureInfo = fields.Str(attribute='measure_info')
    measureStatus = fields.Integer(attribute='measure_status')
    measureTime = fields.DateTime(attribute='measure_time')
    createTime = fields.DateTime(attribute='create_time')
    updateTime = fields.DateTime(attribute='update_time')
