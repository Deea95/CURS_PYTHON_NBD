a = ["a", "b", "c"]
b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
c = {"c1": a, "c2": b, "c3": 42}
obj = "{v1": a, "v2": b, "v3": c}
txt = json.dumps(obj)
print(txt)
{"v1": ["a", "b", "c"], "v2": [[0, 1, 0],
                               {"c1": ["a", "b", "c"], "c2": [[0, 1, 0],
                                                              declared as a
two - dimensional
array(a
matr
