from flask import Blueprint

bp = Blueprint('aide', __name__, url_prefix='/aide', template_folder='templates', static_folder='static')

from . import views
