from flask import render_template

from flask_aide.aide import bp


@bp.route('/codes')
def codes():
    return render_template('aide/codes.html')
