import random

draws = 8
Jar = ["", ""]
Z = ""

def Fill_Jar(S, p):
    Balls_W = round(100 * p)
    Balls_B = 100 - Balls_W

    for i in range(Balls_W):
        Jar[S] += "W"
    for i in range(Balls_B):
        Jar[S] += "B"

def Draw(S):
    rc = random.randint(0, len(Jar[S]) - 1)
    return Jar[S][rc]

Fill_Jar(0, 0.2)
Fill_Jar(1, 0.6)

a = Draw(1)
Z += f"Jar W[{a}], "

for i in range(draws):
    if a == "W":
        a = Draw(0)
        Z += f"Jar W[{a}], "
    else:
        a = Draw(1)
        Z += f"Jar B[{a}], "

print(Z)