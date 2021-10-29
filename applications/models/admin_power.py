import datetime
from applications.models import db, ma
from marshmallow import fields


class Power(db.Model):
    __tablename__ = 'admin_power'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(1))
    code = db.Column(db.String(30))
    url = db.Column(db.String(255))
    open_type = db.Column(db.String(10))
    parent_id = db.Column(db.Integer)
    icon = db.Column(db.String(128))
    sort = db.Column(db.Integer)
    create_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now)
    update_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now)
    enable = db.Column(db.Integer)


# 权限 models 序列化类
class PowerSchema(ma.Schema):
    id = fields.Integer()
    title = fields.Str(attribute="name")
    type = fields.Str()
    code = fields.Str()
    href = fields.Str(attribute="url")
    openType = fields.Str(attribute="open_type")
    parent_id = fields.Integer()
    icon = fields.Str()
    sort = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    enable = fields.Integer()


class PowerSchema2(ma.Schema):  # 序列化类
    powerId = fields.Str(attribute="id")
    powerName = fields.Str(attribute="name")
    powerType = fields.Str(attribute="type")
    powerUrl = fields.Str(attribute="url")
    openType = fields.Str(attribute="open_type")
    parentId = fields.Str(attribute="parent_id")
    icon = fields.Str()
    sort = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    enable = fields.Integer()

