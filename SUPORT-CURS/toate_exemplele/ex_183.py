# 10.4.2 Ex. (183) – Smooth signal
def smooth(a):            Output:


n = len(a)
for i in range(1, n - 1): 5, 6.5, 5.2, 5.6, 3.8, 6.4, 7.2, 8
a[i] = (a[i - 1] + a[i + 1]) / 2
return a
a = [5, 1, 8, 4, 6, 2, 9, 8]
print(smooth(a))
