import os
import posixpath
from datetime import datetime

from flask import current_app as app
from flask import render_template
from flask import request
from werkzeug.exceptions import BadRequest

from flask_aide.aide import bp


@bp.route('/codes')
def codes():
    path = request.args.get('path', '')
    path = posixpath.normpath(path)
    root = os.path.join(app.root_path, path)
    root = os.path.normpath(root)
    if not root.startswith(app.root_path):
        raise BadRequest()

    files = [{'is_dir': True, 'name': '..', 'size': '', 'create_date': datetime.now(), 'modified_date': datetime.now(),
              'param': posixpath.normpath(posixpath.join(path, '..'))}]
    for name in os.listdir(root):
        entity = {'name': name}
        full_path = os.path.join(root, name)
        entity['is_dir'] = os.path.isdir(full_path)
        entity['size'] = '' if entity['is_dir'] else os.path.getsize(full_path)
        entity['create_date'] = datetime.fromtimestamp(os.path.getctime(full_path))
        entity['modified_date'] = datetime.fromtimestamp(os.path.getmtime(full_path))
        entity['param'] = posixpath.join(path, name)
        files.append(entity)

    return render_template('aide/codes.html', files=files)
