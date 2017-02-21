from flask import Flask

from flask_aide import FlaskAide

aide = FlaskAide()
app = Flask(__name__)

aide.init_app(app)

host, port = '0.0.0.0', 8080
app.logger.error('Listen on %s:%s', host, port)
app.logger.error(app.url_map)
app.run(host, port)
