# 5.1.41Ex. (81) – The rule of three simples
a = [5, 1, 8, 4, 6, 2, 9, 8]
Output:
n = len(a)
55.55555555555556 %
max_value = 0
11.11111111111111 %
m = 100
t = []
44.44444444444444 %
for i in range(n):
    if a[i] > max_value:
        max_value = a[i]
for i in range(n):
    p = (m / max_value) * a[i]
    print(f'{p}%')
