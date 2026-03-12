a = [5, 1, 8, 4, 6, 2, 9, 8]
n = len(a)
max_value = 0
m = 100
t = []
for i in range(n):
    if a[i] > max_value:
        max_value = a[i]
        for i in range(n):
            p = (m / max_value) * a [i]
            print(f'{p}%')