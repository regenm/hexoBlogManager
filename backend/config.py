import os

class Config:
    MYSQL_HOST = '192.168.98.130'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'flask_Vue_mysql'
    SECRET_KEY = os.urandom(24)
