from flask import Flask
from flask_cors import CORS

from flask_aide import FlaskAide

aide = FlaskAide()
cors = CORS()
app = Flask(__name__)

aide.init_app(app)
cors.init_app(app)

host, port = '0.0.0.0', 8080
app.logger.error('Listen on %s:%s', host, port)
app.logger.error(app.url_map)
app.run(host, port, debug=True)
