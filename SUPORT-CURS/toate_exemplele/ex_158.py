# 9.2.1 Ex. (158) – Object to JSON
# a Python object...
# ... converted into JSON:
import json

obj = {"v1": 1, "v2": 2, "v3": 3}
txt = json.dumps(obj)

print(txt)
# send JSON:
# print("index.php?obj=" + txt);
