from devapp.app import FLG
from operators.ops.exceptions import Err, OpArgParseError
from operators.ops.tools import Rx, rx

#            raise OpArgParseError(Err.param_not_supported, mode=mode, id=id)


class Join:
    """
    A Join node, turning n messages of the same group into one.

    Supports only data dicts right now, no buffers and such things.

    Defaults:

    * Grouping: same message id.
    * Data confict resolution:

        - Headers of first one win, but payload of second.
        - Rationale:
            - This operator is also our object cache.
            - Objects will be kept in headers - while data enrichment will take time:
                            ┌─────────> NR:DBlookup ──>┐
                        PySockSrc────────────────────>Join ─> PySockSink
    """

    def validate_supported_features(id, mode, **kw):
        # custom is manual in NR:
        if not mode in ('auto', 'manual', 'custom'):
            # TODO: Implement all these neat joining feats:
            raise OpArgParseError(Err.param_not_supported, mode=mode, id=id)

    def parse_args(name, id, timeout, count, mode='auto', **kw):
        """
        The op as normally > 1 inputs, i.e. is following a merge.
        """
        joiner = kw.get('joiner').strip() or 'm[_ids][msg]'   # e.g. d[id]
        joiner = '{%s}' % joiner
        if not count and mode == 'auto' and len(kw['src']) == 2:
            count = 2
        Join.validate_supported_features(**dict(locals()))

        # that always - never cache infinite times, mem will explode:
        rx_timeout = Rx.timer(float(timeout or FLG.op_join_default_timeout))

        def end_of_group(s, count=int(count or 0), timeout=rx_timeout):
            """when is a sequence complete, i.e. join.sends an item"""
            # 'NodeRed: After a message with the msg.complete property set':
            is_complete = s.pipe(rx.filter(lambda x: x.pop('complete', False)))
            if not count:
                return Rx.merge(is_complete, timeout)
            else:
                # we got all, when we can skip count-1 and still produce:
                got_items = s.pipe(rx.skip(count - 1))
                return Rx.merge(got_items, is_complete, timeout)

        def msg_group(msg, joiner=joiner):
            """what dictates two messages to belong together?"""
            # group qulifier. e.g. m[payload]['id']
            return joiner.format(m=msg)

        # how to combine the messages:
        def reducer_(have, msg):
            """combines items of same group to one"""
            try:
                have['payload'].update(msg['payload'])
            except Exception as ex:
                # then we assume the latter message, which took more steps to process
                # has the information - and the first is just for object caching,e.g. a socket
                have['payload'] = msg['payload']
            return have

        grouper = rx.group_by_until(msg_group, None, end_of_group)
        combiner = rx.flat_map(lambda s, r=reducer_: s.pipe(rx.reduce(r)))
        return rx.pipe(
            grouper,
            combiner,
        )


# def dbg(msg, *a):
#     breakpoint()  # FIXME BREAKPOINT
#     return msg


# TODO:
# {'_is_py': True,
#  '_orig_wires': [['6d02057a.aee57c']],
#  'accumulate': True,
#  'build': 'object',
#  'count': '',
#  'id': '1e9d61a4.775c2e',
#  'joiner': '\\n',
#  'joinerType': 'str',
#  'key': 'topic1',
#  'mode': 'auto',
#  'name': '',
#  'property': 'payload',
#  'propertyType': 'msg',
#  'reduceExp': '',
#  'reduceFixup': '',
#  'reduceInit': '',
#  'reduceInitType': '',
#  'reduceRight': False,
#  'src': ['srv', '253c721f.f5770e'],
#  'timeout': '',
#  'type': 'ax-join',
#  'wires': [['6d02057a.aee57c']],
#  'ws': ['6d02057a.aee57c'],
#  'x': 550,
#  'y': 360,
#  'z': 'tests'}
# (Pdb)
