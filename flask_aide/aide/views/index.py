from flask import render_template

from flask_aide.aide import bp


@bp.route('/index')
def index():
    return render_template('aide/index.html')
