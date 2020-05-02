# 管理第三方拓展库
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_extension(app):
    db.init_app(app)
