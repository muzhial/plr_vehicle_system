from applications.models import db
# create intermediate table
user_role = db.Table(
    "admin_user_role",
    db.Column("id", db.Integer, primary_key=True, autoincrement=True),
    db.Column("user_id", db.Integer, db.ForeignKey("admin_user.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("admin_role.id")),
)

