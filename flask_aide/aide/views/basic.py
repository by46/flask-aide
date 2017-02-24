import platform

import flask
from flask import current_app as app
from flask import render_template

from flask_aide.aide import bp


@bp.route('/basic')
def basic():
    system_info = [('System', platform.system()),
                   ('Release', platform.release()),
                   ('Hostname', platform.node()),
                   ('IP', '127.0.0.1'),
                   ('Processor', platform.machine())]

    if platform.system() == 'Linux':
        distribution, version, _ = platform.linux_distribution()
        system_info.append(('Distribution', ' '.join([distribution, version])))

    python_info = [('Implementation', platform.python_implementation()),
                   ('Version', platform.python_version()),
                   ('Compiler', platform.python_compiler()),
                   ('Build Date', platform.python_build()[-1]),
                   ('Bits', platform.architecture()[0])]

    app_info = [('Name', app.name),
                ('Flask Version', flask.__version__),
                ('Import Name', app.import_name),
                ('Root Path', app.root_path),
                ('Static URL Prefix', app.static_url_path),
                ('Static Folder', app.static_folder)]

    blueprints = app.blueprints


    return render_template('aide/basic.html',
                           system_info=system_info,
                           python_info=python_info,
                           app_info=app_info,
                           blueprints=blueprints)
