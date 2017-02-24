import os
from datetime import datetime

from flask import current_app as app
from flask import render_template

from flask_aide.aide import bp


@bp.route('/codes')
def codes():
    root = app.root_path
    files = []
    for name in os.listdir(root):
        entity = {'name': name}
        full_path = os.path.join(root, name)
        entity['is_dir'] = os.path.isdir(full_path)
        entity['size'] = '' if entity['is_dir'] else os.path.getsize(full_path)
        entity['create_date'] = datetime.fromtimestamp(os.path.getctime(full_path))
        entity['modified_date'] = datetime.fromtimestamp(os.path.getmtime(full_path))
        files.append(entity)

    return render_template('aide/codes.html', files=files)
