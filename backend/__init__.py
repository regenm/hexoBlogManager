from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('backend.config.Config')

mysql = MySQL(app)

from backend import routes  # 确保导入 routes 模块

