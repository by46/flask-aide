from flask_aide.aide import bp


class FlaskAide(object):
    def __init__(self, app=None, **kwargs):
        self.options = kwargs
        self.app = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        app.register_blueprint(bp)
