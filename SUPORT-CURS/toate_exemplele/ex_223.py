import json

# data
a = ["a", "b", "c"]

b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

c = {
    "c1": a,
    "c2": b,
    "c3": 42
}

obj = {
    "v1": a,
    "v2": b,
    "v3": c
}

# STORE
txt = json.dumps(obj)

with open('storage.txt', 'w') as file:
    file.write(txt)

# READ
with open('storage.txt', 'r') as file:
    txt = file.read()

obj = json.loads(txt)

# MESSAGE build
msg = ""
msg += "From string:\n" + txt
msg += "\n\nFrom object:\n" + obj['v1'][1]
msg += "\n" + str(obj['v2'][0][1])
msg += "\n" + str(obj['v3']['c2'])
msg += "\n" + str(obj['v3']['c2'][1][1])

print(msg)