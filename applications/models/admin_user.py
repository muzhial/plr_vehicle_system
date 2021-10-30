import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from applications.models import db, ma
from marshmallow import fields
from applications.models import admin_user_role


class User(db.Model, UserMixin):
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    realname = db.Column(db.String(20))
    avatar = db.Column(
        db.String(255),
        default="")
    remark = db.Column(db.String(255), comment='remark')
    password_hash = db.Column(db.String(128))
    enable = db.Column(db.Integer, default=0)
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)
    update_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now)
    role = db.relationship(
        'Role',
        secondary="admin_user_role",
        backref=db.backref('user'),
        lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserSchema(ma.Schema):
    id = fields.Integer()
    username = fields.Str()
    realname = fields.Str()
    enable = fields.Integer()
    create_at = fields.DateTime()
    update_at = fields.DateTime()

