c = [
def matrix_alphabet(t):
    a = []
    n = len(t)
    m = len(t[0])
    for i in range(n):
        for j in range(m):
            q = 1
            for k in range(len(a) +
            if k < len(a) and t[
            q = 0
            if q == 1:
                print(matrix_alphabet(c))