from flask_aide.aide import bp
from flask_aide.aide.filters import FILTERS


class FlaskAide(object):
    def __init__(self, app=None, **kwargs):
        self.options = kwargs
        self.app = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        [app.add_template_filter(f) for f in FILTERS]

        app.register_blueprint(bp)
