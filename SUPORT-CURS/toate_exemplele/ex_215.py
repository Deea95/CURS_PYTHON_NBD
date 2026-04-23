import random

def mutate(a):
    m = len(a)
    n = 200
    b = [0] * m

    for i in range(n):
        S = 0  # score

        for j in range(m):
            b[j] = round(random.random())

            # complementary array
            if b[j] != a[j]:
                S += 1

        if S >= m:
            return b

    return "not found by random means."

a = [1, 0, 0, 1, 1, 1, 0]
print(mutate(a))