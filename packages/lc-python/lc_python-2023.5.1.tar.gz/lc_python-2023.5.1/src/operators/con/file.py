import os, stat, time
import sys

from devapp.app import app
from devapp.tools import get_deep, project, repl_dollar_var_with_env_val, read_file
from node_red.tools import js
from operators.con import con_params
from operators.ops.tools import rx_operator


def normalize_filename(fn, clear=None):
    if fn in ('-', 'stdout'):
        return sys.stdout
    elif fn == 'stderr':
        return sys.stderr
    fn = repl_dollar_var_with_env_val(fn)
    if fn.startswith('.'):
        fn = os.path.abspath(fn)
    elif not fn.startswith('/'):
        fn = project.root() + '/' + fn
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    if clear:
        open(fn, 'w').close()
    return open(fn, 'ab')


def byte_sep(sep):
    if isinstance(sep, str):
        return sep.encode('utf-8')
    elif isinstance(sep, int):
        sep = [sep]
    return b''.join([chr(i).encode('utf-8') for i in sep])


class file:
    name = 'file'
    url = ''

    def watch(observer, filename, interval=10, push_content=False):
        """a dependency free polling file change monitor"""
        last = 0
        exists = os.path.exists
        fn = filename
        while True:
            if callable(filename):
                fn = filename()
            if exists(fn):
                s = os.stat(fn)[stat.ST_MTIME]
                if s != last:
                    last = s
                    app.debug('file changed', fn=fn)
                    data = {'fn': fn, 'mtime': last}
                    if push_content:
                        data['content'] = read_file(fn, dflt='')
                    observer.on_next(data)
            time.sleep(interval)

    class con_defaults:
        filename = '-'
        sep = 10  # = \n
        clear = True
        write = 'payload'
        flush = False

    @classmethod
    def snk(cls, is_rx=True, **cfg):
        con = con_params(cls, defaults=cls.con_defaults)
        con.update(cfg)
        # fn = repl_dollar_var_with_env_val(fn)
        # if fn.startswith('./'):
        #     fn = os.path.abspath(fn)
        # if not fn.startswi
        # dn = os.path.dirname(filename)
        # sep = sep.encode('utf-8')
        # if not os.path.exists(dn):
        #     os.makedirs(dn)
        # if clear:
        #     os.unlink(filename) if os.path.exists(filename) else 0
        # fd = [0]

        def open_fd(con=con):

            try:
                con['fd'] = normalize_filename(con['filename'], clear=con['clear'])
            except Exception as exc:
                app.die('Cannot open file sink', exc=exc, **con)
            try:
                con['bsep'] = byte_sep(con['sep'])
            except Exception as exc:
                app.die('Cannot build byte seperator', exc=exc, **con)

        def write(data, msg, con=con, _conv=conv):
            write = con['write']
            d = (
                msg
                if write == 'msg'
                else data
                if write == 'payload'
                else get_deep(write, msg, sep='.', create=True, dflt=None)
            )
            try:
                d = _conv.get(type(d), _conv['dflt'])(d)
                fd = con['fd']
                fd.write(d + con['bsep'])
                fd.flush() if con['flush'] else 0
            except Exception as ex:
                app.error('could not write', fn=con['filename'], exc=ex)

        def close_fd(con=con):
            try:
                con['fd'].close()
            except Exception as ex:
                app.error('could not close', fn=con['filename'])

        return rx_operator(
            on_subscription=open_fd, on_next=write, on_completed=close_fd
        )


conv = {
    bytes: lambda x: x,
    str: lambda x: x.encode('utf-8'),
    'dflt': lambda x: js(x).encode('utf-8'),
}
