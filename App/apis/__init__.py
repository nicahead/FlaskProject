from App.apis.first_blue import blue


def init_view(app):
    app.register_blueprint(blue)
