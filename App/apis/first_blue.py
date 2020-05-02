from flask import Blueprint

from App.models.user import User

# （蓝图的名字，导入的名字）
blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return "主页"


@blue.route('/addUser')
def addUser():
    user = User()
    user.username = "test"
    user.save()
    return '保存成功'

