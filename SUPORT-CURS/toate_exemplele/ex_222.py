import base64

ori = "this is a text!"

# Encode a string.
enc = base64.b64encode(ori.encode()).decode()

# Decode the string.
dec = base64.b64decode (enc) .decode()

print(enc)
print(dec)