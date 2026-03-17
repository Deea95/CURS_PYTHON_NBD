# 8.1.6 Ex. (130) – Random integers from 0 to 99 in an array
import random

a = []

n = 10

for k in range(n):
    a.append(random.randint(0, 99))
print(a)
