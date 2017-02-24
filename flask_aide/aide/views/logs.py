from flask import render_template

from flask_aide.aide import bp


@bp.route('/logs')
def logs():
    return render_template('aide/logs.html')
