import random

Jar = ["WWBBBBBBBB", "WWWWWBBBBB"]

draws = 17
Z = ""

def Draw(S):
    # Choose a random character
    rc = random.randint(0, len(Jar[S]) - 1)
    ball = Jar[S][rc]
    return ball

# Initial draw
a = Draw(1)
Z += f"Jar W[{a}], "

for i in range(1, draws + 1):
    if a == "W":
        a = Draw(0)
        Z += f"Jar W[{a}], "
    else:
        a = Draw(1)
        Z += f"Jar B[{a}], "

print(Z)