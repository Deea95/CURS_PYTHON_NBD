# txt is text received in JSON format.
# Convert JSON into a Python object:
    # JSON text.
    txt = '{"v1":1,"v2":2,"v3":3}'
    # Parse JSON to create
    # a Python object.
    obj = json.loads(txt)
    print(obj['v1'])
    print(obj['v2'])
    print(obj['v3'])