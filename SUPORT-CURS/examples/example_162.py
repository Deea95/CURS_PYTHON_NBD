txt = '{"v1":["a","b","c"],"v2":' + \
      '[[0,1,0],[1,1,1],[0,1,0]]' + \
      ',"v3":{"c1":["a","b","c"]' + \
      ',"c2":[[0,1,0],[1,1,1],[0' + \
      ',1,0]],"c3":42}}'
obj = json.loads(txt)
a = obj['v1']
b = obj['v2']
c = obj['v3']
print(a)
print(b)
print(c['c1'])
print(c['c2'])
print(c['c3'])
pairs, namely: (i)
"c1" is associated
with a
    similar
    to
    the
    array in "v1."(ii)
    "c2" is assoc
    code
    prints
    these
    extracted
    values
    for user in
        is to
    assign
    parts
    of
    one
    object(i.e.obj)
    into
    values
    found in its
    properties(i.e.c1, c2, an
