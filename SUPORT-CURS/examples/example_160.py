a = ["a", "b", "c"]
b = [
c = {"c1": a, "c2": b, "c3": 42}
# Create an object-like dictionary.
obj = "{v1": a, "v2": b, "v3": c}
# Serialize the dictionary
# to a JSON string.
txt = json.dumps(obj)
print(txt)