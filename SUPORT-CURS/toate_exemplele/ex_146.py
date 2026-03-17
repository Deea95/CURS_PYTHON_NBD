# 8.3.1 Ex. (146) – Replacement for repeat loops with recursion
# replacement for                  Output:
# repeat loops.
def for_loop(a, b, r):
    a += 1
    # do stuff from
    r += 5
    # to here
    if a >= b:
        return r
    else:
        return for_loop(a, b, r)


a = for_loop(0, 7, 0)
print(a)
Here, we
have
a
custom
recursive
function
called
for loop that may serve as a replace-
ment
for traditional repeat loops.The variable a is assigned the result of calling the for
loop
function
with the initial parameters 0 for a, 7 for b, and 0 for r.The function is
intended
to
simulate
the
behavior
of
a
repeat
loop.Within
the
for loop function, variable
