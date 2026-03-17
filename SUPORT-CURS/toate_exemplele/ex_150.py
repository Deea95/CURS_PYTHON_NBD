# 8.3.5 Ex. (150) – Generate a sequence recursively
def sequence(n, m, i, t):          Output:


m.append(n)
i += 1
A
sequence:
[5, 7, 11, 19, 35]
if i >= t:
    return m
else:
    return sequence((n - 1) + (n - 2), m, i, t)
    # Testing the function
# and printing the sequence.
d = sequence(5, [], 0, 5)
print("A sequence:\n[", d, "]")
