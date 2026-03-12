# a Python object...
# ... converted into JSON:
    obj = {"v1": 1, "v2": 2, "v3": 3}
    txt = json.dumps(obj)
    print(txt)
    # send JSON:
        # print("index.php?obj=" + txt);