# 8.3.7 Ex. (152) – Sum all from array recursively
def sum_array(n, q, r):            Output:


r += q[n]
Sum
array: [25]
if n <= 0:
    return r
else:
    return sum_array(n - 1, q, r)
q = [1, 3, 3, 4, 5, 9]
f = sum_array(len(q) - 1, q, 0)
print(f"Sum array: [{f}]")
This
time, the
code
demonstrates
a
recursive
function
for summing the elements of an
