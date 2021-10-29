import datetime
from applications.models import db, ma
from marshmallow import fields
from applications.models import admin_role_power


class Role(db.Model):
    __tablename__ = 'admin_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(255))
    enable = db.Column(db.Integer)
    remark = db.Column(db.String(255))
    details = db.Column(db.String(255))
    sort = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now)
    power = db.relationship(
        'Power',
        secondary="admin_role_power",
        backref=db.backref('role'))


class RoleSchema(ma.Schema):
    id = fields.Integer()
    roleName = fields.Str(attribute="name")
    roleCode = fields.Str(attribute="code")
    enable = fields.Str()
    remark = fields.Str()
    details = fields.Str()
    sort = fields.Integer()
    create_at = fields.DateTime()
    update_at = fields.DateTime()

