import os
import json

obj = []
n = 0
s = 0

file_path = os.path.join(os.path.dirname(__file__), "log.txt")

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
            obj.append(json.loads(line.strip()))
            s += obj[n]["v2"]
            n +=1
            
for i in range(n):
    print(obj[i])

print(obj[1]["v2"])

print(obj)

print(s)