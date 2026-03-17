# 8.3.6 Ex. (151) – Generate fibonacci recursively
def fibonacci(n, m, t):            Output:


n += 1
m.append(m[n - 1] + m[n - 2])
Fibonacci:
[0, 1, 2, 3, 5, 8]
if n >= t:
    return m
else:
    return fibonacci(n, m, t)
e = fibonacci(2, [0, 1, 2], 5)
print("Fibonacci:\n[" + ', '.join(map(str, e)) + "]")
