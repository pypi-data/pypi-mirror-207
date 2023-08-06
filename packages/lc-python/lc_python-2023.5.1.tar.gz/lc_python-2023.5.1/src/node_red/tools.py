#!/usr/bin/env python

import json

import ujson


def to_str(obj):
    try:
        return obj.decode('utf-8')
    except:
        return str(obj)


# js is superdangerous - will block hanging if there are objects like 'ws' inside!!
def js(struct, ensure_ascii=False, reject_bytes=False):
    try:
        # fails when objects are in, e.g. connection sockets:
        return ujson.dumps(struct, ensure_ascii=ensure_ascii, reject_bytes=reject_bytes)
    except:
        return json.dumps(struct, default=to_str)


jp = lambda s1: ujson.loads(s1)


to_list = (
    lambda s, sep=',': s
    if isinstance(s, list)
    else list(s)
    if isinstance(s, tuple)
    else [str(i).strip() for i in s.split(sep)]
)
