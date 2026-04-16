"""
import json

student = {
    "nume": "Popescu",
    "varsta": 21,
    "note": [9,10,8]
}

with open("student.json", "w") as f:
    json.dump(student, f)
"""
# citire json
"""
import json
with open("student.json", "r") as f:
    student = json.load(f)
print(student["nume"])
print(student["varsta"])
"""
# Ex combinare JSON + procesare
"""
import json

with open("student.json", "r") as f:
    data = json.load(f)

media = sum(data["note"]) / len(data["note"])
print("Media:", media)
"""

"""
# Excel, citire, scriere manipulare:
import pandas as pd

# creare tabel
df = pd.DataFrame({
    "nume": ["Ana", "Ion"],
    "nota": [9, 7]
})

# salvare Excel
df.to_excel("note.xlsx", index=False)

# citire Excel
df2 = pd.read_excel("note.xlsx")

# manipulare
df2["nota"] = df2["nota"] + 1

print(df2)
"""
"""
# Generare data random + fisiere mari
import random

with open("date_mari.txt", "w") as f:
    for i in range(100000):  # fișier mare
        numar = random.randint(1, 1000)
        f.write(str(numar) + "\n")
"""
"""
# Procesare fara a incarca tot in memorie
total = 0

with open("date_mari.txt", "r") as f:
    for linie in f:
        total += int(linie)
print(total)
"""
"""
#
#media
total = 0
count = 0

with open("date_mari.txt", "r") as f:
    for linie in f:
        total += int(linie)
        count += 1

if count > 0:
    media = total / count
    print(media)
else:
    print("Fisierul este gol")
"""
"""
import tkinter as tk

def afiseaza():
    text = entry.get()
    label.config(text="Ai scris: " + text)

root = tk.Tk() #fereastra aplicatiei
root.title("Exemplu GUI")

entry = tk.Entry(root)
entry.pack()

buton = tk.Button(root, text="Apasa", command=afiseaza)
buton.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
"""
"""

import tkinter as tk
import random

def afiseaza():
    text = entry.get()
    with open("test2.txt", "w") as f:
        for i in range(int(text)):
            numar = random.randint(1, 10)
            f.write(str(numar) + "\n")

    # fisier mare

root = tk.Tk()
root.title("Exemplu GUI")

entry = tk.Entry(root)
entry.pack()

buton = tk.Button(root, text="Apasa", command=afiseaza)
buton.pack()
"""
"""
import tkinter as tk

def afiseaza():
    text = entry.get()
    label.config(text="Ai scris: " + text)

root = tk.Tk()
root.title("Exemplu GUI")
root.geometry("400x250") # dimensiune fereastra

# Input
entry = tk.Entry(root)
entry.place(x=100, y=40, width=200, height=30)

# Buton
buton = tk.Button(root, text="Apasa", command=afiseaza)
buton.place(x=150, y=90, width=100, height=40)

# Label rezultat
label = tk.Label(root, text="")
label.place(x=100, y=150, width=200, height=30)

root.mainloop()
"""
"""
import tkinter as tk

def calc():
    a = int(e1.get())
    b = int(e2.get())
    rez.config(text=str(a + b))

root = tk.Tk()
root.geometry("300x200")

e1 = tk.Entry(root)
e1.place(x=50, y=30, width=80)

e2 = tk.Entry(root)
e2.place(x=170, y=30, width=80)

btn = tk.Button(root, text="+", command=calc)
btn.place(x=120, y=70, width=60, height=30)

rez = tk. Label(root, text="")
rez.place(x=100, y=120, width=100, height=30)

root.mainloop()
"""
"""
import tkinter as tk

def rosu():
    root.config(bg="red")

def verde():
    root.config(bg="green")

root = tk.Tk()
root.geometry("300x200")

b1 = tk.Button(root, text="Rosu", command=rosu)
b1.place(x=50, y=80, width=80, height=40)

b2 = tk.Button(root, text="Verde", command=verde)
b2.place(x=170, y=80, width=80, height=40)

root.mainloop()
"""
"""
#daca parola este gresita, modificati background-ul in rosu
import tkinter as tk

def verifica():
    if entry.get() == "1234":
        label.config(text="Corect")
        root.config(bg="green")   # fundal verde
    else:
        label.config(text="Gresit")
        root.config(bg="red")     # fundal rosu

root = tk.Tk()
root.geometry("300x200")

entry = tk.Entry(root, show="*")
entry.place(x=80, y=40, width=140)

btn = tk.Button(root, text="Check", command=verifica)
btn.place(x=100, y=80, width=100, height=30)

label = tk.Label(root, text="")
label.place(x=100, y=130, width=100)

root.mainloop()
"""
"""
import tkinter as tk

def citeste():
    with open(r"date_mari.txt", "r") as f:
        text = f.read()
        label.config(text=text[:50])

root = tk.Tk()
root.geometry("400x200")

btn = tk.Button(root, text="Citeste fisier", command=citeste)
btn.place(x=120, y=40, width=150, height=40)

label = tk.Label(root, text="")
label.place(x=50, y=120, width=300, height=40)

root.mainloop()
"""
"""
import tkinter as tk

def citeste():
    with open(r"date_mari.txt", "r") as f:
        text = f.read()
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, text)

root = tk. Tk()
root.geometry("500x300")

btn = tk.Button(root, text="Citeste fisier", command=citeste)
btn.place(x=150, y=20, width=200, height=40)

# Textbox
textbox = tk.Text(root)
textbox.place(x=50, y=80, width=350, height=180)

# Scrollbar vertical
scroll = tk.Scrollbar(root, command=textbox.yview)
scroll.place(x=400, y=80, height=180)

# Legătură Text + Scroll
textbox.config(yscrollcommand=scroll.set)

root.mainloop()
"""
"""
import tkinter as tk

def smooth(a):
    n = len(a)
    b = a.copy()
    for i in range(1, n - 1):
        b[i] = (a[i - 1] + a[i + 1]) / 2
    return b


def calculeaza():
    a = [5, 1, 8, 4, 6, 2, 9, 8]
    rezultat = smooth(a)

    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, str(rezultat))


root = tk.Tk()
root.geometry("350x250")

btn = tk.Button(root, text="Calculeaza", command=calculeaza)
btn.place(x=120, y=40, width=100, height=30)

textbox = tk.Text(root, height=6, width=30)
textbox.place(x=60, y=100)

root.mainloop()

# 10.4.6 Ex. (187) – Alphabet detection
# ALPHABET DETECTION.
def alpha(c):

    a = []
    t = list(c)
    k = len(t)
    for i in range(k):
        q = 1
        for j in range(len(a)):
            if t[i] == a[j]:
                q = 0
        if q == 1:
         a.append(t[i])
    return a
print(alpha('uiuhd87wqsaidhsad'))
"""
"""
# 10.4.7 Ex. (188) – Alphabet detection on matrices
c =[
   [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
   [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
   [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
   [0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
   [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
   [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
   [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
   [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
   ]

def matrix_alphabet(t):
    a = []
    n = len(t)
    m = len(t[0])
    for i in range(n):
        for j in range(m):
            q = 1
            for k in range(len(a) + 1):
                if k < len(a) and t[i][j] == a[k]:
                    q = 0
            if q == 1:
                a.append(t[i][j])
    return a


print(matrix_alphabet(c))

# 10.5.1 Ex. (189) – Low level native sort and eliminate duplicates (I)
a = {}

b = [3, 6, 2, 78, 99, 1, 4]
r = 0
n = len(b)
for i in range(n):
    a[b[i]] = b[i]
m = max(a.keys()) + 1
for j in range(m):
    if j in a:
        b[r] = a[j]
        r += 1
print(b)

"""
"""
# 10.7.1 Ex. (194) – Return an array with proportions (relative frequencies)
def p(a):
    max_value = max(a)
    n = len(a)
    m = 100
    # Preallocate the list
    # with the required size.
    t = [''] * n
    for i in range(n):
        t[i] = str(round((m / max_value) * a[i])) + '%'
    return t
a = [5, 1, 8, 4, 6, 2, 9, 8]
print(p(a))

# or another version:
def p(a):
    max_value = max(a)
    n = len(a)
    m = 100
    t = []
    for i in range(n):
        t.append(str(round((m / max_value) * a[i])) + '%')
    return t

a = [5, 1, 8, 4, 6, 2, 9, 8]
print(p(a))
"""
# ex 196
def p(a, b):
    n = len(a)
    m = [0, 0]

    # calcul medii
    for i in range(n):
        m[0] += a[i]
        m[1] += b[i]

    m[0] = m[0] / n  # mean a
    m[1] = m[1] / n  # mean b

    s0 = 0
    s1 = 0
    s2 = 0

    # calcul coeficient
    for i in range(n):
        s0 += (a[i] - m[0]) * (b[i] - m[1])
        s1 += (a[i] - m[0]) ** 2
        s2 += (b[i] - m[1]) ** 2

    r = s0 / (s1 * s2) ** 0.5
    return r


a = [6, 8, 10]
b = [12, 10, 20]

print(p(a, b))
