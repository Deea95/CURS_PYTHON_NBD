# 9.2.3 Ex. (160) – Anything to object to string
a = ["a", "b", "c"]
b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
c = {"c1": a, "c2": b, "c3": 42}
# Create an object-like dictionary.
obj = "{v1": a, "v2": b, "v3": c}
# Serialize the dictionary
# to a JSON string.
txt = json.dumps(obj)
print(txt)
{"v1": ["a", "b", "c"], "v2": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "v3":
{"c1": ["a", "b", "c"], "c2": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "c3": 42}}
