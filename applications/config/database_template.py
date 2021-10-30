# database connection config
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'PlrVehicleSys'
USERNAME = 'your-db-name'
PASSWORD = 'your-db-passwd'

DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}" \
         f"?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_RECYCLE=8

