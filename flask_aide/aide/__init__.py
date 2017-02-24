import os.path

from flask import Blueprint

template_folder = os.path.join(__file__, '..', 'templates')
template_folder = os.path.normpath(template_folder)

bp = Blueprint('aide', __name__, url_prefix='/aide', template_folder='templates', static_folder='static')

from . import views
