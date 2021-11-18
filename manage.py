from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from main import app
from applications.models import db

manager = Manager(app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)  # 创建数据库映射命令

# import models 不能省
from applications.models import (
    admin_user, admin_role, admin_power, admin_log, admin_photo,
    admin_measure_data, admin_role_power, admin_user_role)

manager.add_command('start',
                    Server(
                        host='0.0.0.0',
                        port=8080,
                        use_debugger=True))


if __name__ == '__main__':
    manager.run()
