"""
Provides our customized Node-RED

- npm install of all node modules
- style adapations
- starter files bin/hub, bin/hubdebug

To understand which function is run when, check the resources.py
"""

from devapp.app import app, do, system
from devapp.tools import project, read_file, write_file, offset_port, exists
import os
import json
import time

j = os.path.join


def set_ax_style(dest):
    app.info('styling Node-RED')
    here = os.getcwd()
    os.chdir(dest + '/node_modules/node-red')
    import devapp as d

    rpl = os.path.dirname(d.__file__) + '/third/rpl'

    def r(*ft):
        app.info('replacing', colors=ft)
        cmd = rpl + ' -qiR "%s" "%s" .' % ft
        err = os.system(cmd)
        if err:
            app.die('Could not color replace', cmd=cmd)

    r('8c101c', '8bd124')  # deploy button
    r('AD1625', '89bd12')  # done button
    r('6e0a1e', '6bb104')  # hover button (done)
    os.chdir(here)
    ico = dest + '/node_modules/@node-red/editor-client/public/red/images/node-red.svg'
    app.info('icon', ico=ico)
    write_file(ico, read_file(dest + '/ax/icons/ax_fit.svg'))


#     t = '/node_modules/node-red-contrib-theme-midnight-red/midnight.css'
#     app.info('editor theme', theme=t)
#     fn = dest + '/settings.js'
#     s, r = read_file(fn).splitlines(), []
#     while s:
#         line = s.pop(0)
#         if t in line and line.lstrip().startswith('css:'):
#             line = 'css: "%s"' % (dest + t)
#         r.append(line)
#     write_file(fn, '\n'.join(r))


def project_name():
    return project.root().rsplit('/', 1)[-1]


def nr_user_dir():
    dn = os.path.dirname
    d = dn(dn(__file__)) + '/js/nodered'
    return d


def nr_project_dir():
    return nr_user_dir() + '/projects/' + project_name()


def config():
    n = project_name()
    return {
        'fn': '.config.projects.json',
        'content': {'activeProject': n, 'projects': {n: {'credentialSecret': False}}},
    }


default_flow = [
    {'id': 'first_tab', 'type': 'tab', 'label': 'Flow 1',},
    {
        'id': 'axhub.%s' % int(time.time()),
        'type': 'ax-hub',
        'z': 'first_tab',
        'name': 'AX-Hub',
        'x': 100,
        'y': 100,
        'wires': [[]],
    },
]


def flows(api):
    c = api.constant('fn_flows', '')
    if c:
        if not exists(c):
            app.die('Default flows.json file not found', expected=c)
        app.info('Copying default flows.json', flowfile=c)
        f = json.loads(read_file(c))

    else:
        f = default_flow
    return {'fn': 'flows.json', 'content': f}


def package():
    return {
        'fn': 'package.json',
        'content': {
            'name': project_name(),
            'description': project_name(),
            'version': '0.0.1',
            'dependencies': {},
            'node-red': {
                'settings': {
                    'flowFile': 'flows.json',
                    'credentialsFile': 'flows_cred.json',
                }
            },
        },
    }


def ax_npm_install_and_link_project(rsc, install=False, verify=False, **kw):
    d = nr_user_dir()
    dp = nr_project_dir()

    if verify:
        if not exists(project.root() + '/flows.json'):
            return app.warn('No flows.json')
        if not exists(dp):
            return app.warn('Project not yet linked', dir=dp)
        fn = d + '/package-lock.json'
        s = read_file(fn, dflt='')
        if 'node-red-contrib-axiros' in s:
            return 'node-red-contrib-axiros present in package-lock'
        else:
            app.warn('Nodejs not postinstalled', missing=fn)

    if not install:
        return

    # copy_default_files(dest=d)
    npm = kw['api'].rsc_path(rsc)
    cmd = 'export PATH="%s:$PATH"; cd "%s" && "%s/npm" install ' % (npm, d, npm)
    do(system, cmd)
    set_ax_style(dest=d)
    os.makedirs(nr_user_dir() + '/projects/', exist_ok=True)
    link = lambda: do(system, 'ln -s "%s" "%s"' % (project.root(), dp), ll=30)
    if exists(dp):
        if os.path.islink(dp):
            if os.readlink(dp) == project.root():
                app.info('Project linked already')
            else:
                app.info('Unlinking old project dir')
                os.unlink(dp)
                link()
        else:
            app.warn('Present but no link (copied?)', project_nr_path=dp)
            app.info('Leaving unchanged', project_nr_path=dp)
    else:
        link()
    api = kw['api']
    p = project.root()
    for m in config(), package(), flows(api):
        fn = p + '/' + m['fn']
        if not exists(fn):
            write_file(fn, json.dumps(m['content'], indent=4))


# ------------------------------------------------------------------- provided
title = lambda api: api.constant('hub_title', 'AX-Hub')


def hub(dbg=False, **kw):
    d = nr_user_dir()
    p, fn = project.root(), config()['fn']
    sf = p + '/settings.js'
    ls = ' \\\n  '
    pname = project.root().rsplit('/', 1)[-1]
    hub = (
        'node'
        + ls
        + '  node_modules/node-red/red.js --settings $fn_settings --title "%s" --port %s -u .'
    )
    hub = hub % (title(kw['api']), offset_port(1880))
    cmd = kw['cmd'].replace('hub', hub).replace(' --', ls + '  --')
    pe = [
        'cd "%s"' % d,
        'cp "%s/%s" "%s"' % (p, fn, '.config.projects.json'),
        '',
        '# Configuring Node-RED to use project settings file when present:',
        'fn_settings=settings.js; pname="%s"' % pname,
        'psfn="%s/settings.js"; test -e "$psfn" && {' % p,
        '    cp "$psfn" "./$pname.js"',
        '    fn_settings="$pname.js"',
        '}',
        '',
        '# Title of UI:',
        'export ax_product="%s"' % title(kw['api']),
        '',
    ]
    return {'cmd': cmd, 'pre_exec': pe}


def hubdebug(**kw):
    kw['cmd'] = 'hub'
    s = hub(dbg=True, **kw)
    s['cmd'] = 'node --inspect-brk=1882 ' + s['cmd'].split(' ', 1)[1]
    return s


def npm(cmd, rsc, pth, **kw):
    return ':cd "%s" && npm ' % nr_user_dir()


class node:
    npm = npm
    hub = hub
    hubdebug = hubdebug
    ax_npm_install_and_link_project = ax_npm_install_and_link_project
