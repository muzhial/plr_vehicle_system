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
    parent_id = db.Column(db.Integer)
    create_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now)
    update_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now)
    enable = db.Column(db.Integer)


class PowerSchema(ma.Schema):
    id = fields.Integer()
    title = fields.Str(attribute="name")
    type = fields.Str()
    code = fields.Str()
    href = fields.Str(attribute="url")
    parent_id = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    enable = fields.Integer()


class PowerSchema2(ma.Schema):
    powerId = fields.Str(attribute="id")
    powerName = fields.Str(attribute="name")
    powerType = fields.Str(attribute="type")
    powerCode = fields.Str(attribute='code')
    powerUrl = fields.Str(attribute="url")
    parentId = fields.Str(attribute="parent_id")
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    enable = fields.Integer()

