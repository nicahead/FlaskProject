from flask import Flask

from App.config.settings import envs
from App.extensions import init_extension
from App.apis import init_view


def create_app(env):
    app = Flask(__name__)

    # 加载配置，env从manager传进来，可以在环境变量里获取
    app.config.from_object(envs.get(env))
    # 初始化拓展库，拓展库中初始化models等
    init_extension(app)
    # 初始化路由
    init_view(app)
    return app
