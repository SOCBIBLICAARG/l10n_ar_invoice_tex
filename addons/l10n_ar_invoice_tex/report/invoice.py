import re


def take(s, prefix="", suffix=""):
    if not s: return False
    prefix_re = '.*'.join([ re.escape(w) for w in re_label.split(prefix or '')])
    suffix_re = '.*'.join([ re.escape(w) for w in re_label.split(suffix or '')])
    m = re.search(prefix_re + r"(\d+)" + suffix_re, s)
    return m and m.group(1) or False


def flatdate(d):
    return d.replace('-', '') if d else "000000"


def is_class(o, cls):
    dc = o.journal_id.journal_class_id.document_class_id
    return dc and dc.name and dc.name in cls


def cuit_format(c):
    cuit_string = '{0}-{1}-{2}'.format(c[:2], c[2:-1], c[-1]) \
        if len(c) > 4 else c
    return cuit_string


def codename_format(o):
    dc = o.journal_id.journal_class_id.document_class_id
    return dc.name if dc else 'X'


def type_format(o):
    jc = o.journal_id.journal_class_id
    return (jc.name.split('[')[0]).strip() if jc and jc.name else 'Undefined'
