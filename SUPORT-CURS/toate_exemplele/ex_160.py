# 9.2.3 Ex. (160) – Anything to object to string
a = ["a", "b", "c"]
b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
c = {"c1": a, "c2": b, "c3": 42}
# Create an object-like dictionary.
obj = {"v1": a, "v2": b, "v3": c}
# Serialize the dictionary
# to a JSON string.
import json
txt = json.dumps(obj)
print(txt)

