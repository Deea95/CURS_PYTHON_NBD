# 9.2.1 Ex. (158) – Object to JSON
# a Python object...          Output:
# ... converted into JSON:
obj = {"v1": 1, "v2": 2, "v3": 3}
txt = json.dumps(obj)
print(txt)
# send JSON:
# print("index.php?obj=" + txt);
