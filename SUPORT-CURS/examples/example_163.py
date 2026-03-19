txt = '{"v1":["a","b","c"],"v2":' + \
      '[[0,1,0],[1,1,1],[0,1,0]]' + \
      ',"v3":{"c1":["a","b","c"]' + \
      ',"c2":[[0,1,0],[1,1,1],[0' + \
      ',1,0]],"c3":42}}'
obj = json.loads(txt)
a = []
for i in obj['v3']['c1']:
    a.append(i)
print(a)
(obj).This
code
begins
by
defining
a
variable
(iii)
The “v3” key
has
an
object as its
value
“c3”.(iv)
The “c1” key
has
an
array as its
v
(vi)
The “c3” key
has
a
numerical
value, w
