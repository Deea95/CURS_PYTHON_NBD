"""
# 10.7.6 Ex. (199) – Shannon entropy
import math

def entropy(c):
    a = alpha(c)
    n = len(a)
    k = len(c)
    e = 0

    for i in range(n):
        r = len(c.replace(a[i], ''))
        a[i] = (k - r) / k
        # e += -a[i] * log(2, a[i])
        e += a[i] * log(2, 1 / a[i])
    return e
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

def log(n, v):
    return math.log(v) / math.log(n)


print(entropy('uiuhd87wqsaidhsad'))
print(entropy('aaaaabbbbb'))
print(entropy('ababababababababa'))
print(entropy('aabbbbbbbbbbbbbbb'))
"""
"""
# 11.1.1 Ex. (207) – Spectral forecast for signals in Python.

# Spectral forecast for signals in Python.

A = '10.3,23.4,44.8,63.2,44.1,35.1,46.5,62.6,50.4'
B = '18.8,43.1,52.2,45.5,46.8,46.6,67.9,66.3,70.4'
M = ''

tA = A.split(',')
tB = B.split(',')

maxA = max(map(float, tA))
maxB = max(map(float, tB))
max_value = max(maxA, maxB)

d = 33

for i in range(len(tA)):
    v=((d/maxA)*float(tA[i]))+(((max_value-d)/maxB)*float(tB[i]))
    M += '{:.2f}'.format(v)
    if i < len(tA)-1:
        M += ','
print('Signal A:' + A)
print('Max(A[i]):' + str(maxA))
print('Signal M:' + M)
print('Signal B:' + B)
print('Max(B[i]):' + str(maxB))
"""
"""
# Exemplul 214 - Show similarities between two strings by sequence alignment
# Local sequence alignment algorithm (Smith-Waterman approach)

def f(a1, a2):
    if a1 == a2:
        return Match
    else:
        return Mismatch


Match = 2
Mismatch = -1
gap = -2

s0 = '1100111111111001'
s1 = '00000011111111100000'

AA = ""
AM = ""
AB = ""
e = ' '
m = []
s = []
MMax = 0
MMin = 0
x = 0
y = 0

# Matrix initialization and completion.
s = [list(s0), list(s1)]
n_0 = len(s[0]) + 1
n_1 = len(s[1]) + 1

for i in range(n_0):
    m.append([])
    for j in range(n_1):
        m[i].append(0)

        if i == 1 and j > 1:
            m[i][j] = m[i][j - 1] + gap
        if j == 1 and i > 1:
            m[i][j] = m[i - 1][j] + gap

        if i > 1:
            m[i][0] = s[0][i - 2]
        if j > 1:
            m[0][j] = s[1][j - 2]

        if i > 1 and j > 1:
            A = m[i - 1][j - 1] + f(m[i][0], m[0][j])
            B = m[i - 1][j] + gap
            C = m[i][j - 1] + gap
            D = 0
            m[i][j] = max(A, B, C, D)

            if m[i][j] > MMax:
                MMax = m[i][j]
                x = i
                y = j
            if m[i][j] < MMin:
                MMin = m[i][j]

# Traceback & text alignment.
i = x
j = y
r1 = 0
r2 = 0

while i >= 2 or j >= 2:
    Ai = m[i][0]
    Bj = m[0][j]

    # Verificăm din ce direcție a venit scorul maxim
    A = m[i - 1][j - 1] + f(Ai, Bj)
    B = m[i - 1][j] + gap
    C = m[i][j - 1] + gap

    if i >= 2 and j >= 2 and m[i][j] == A:
        AA = Ai + AA
        AB = Bj + AB
        AM = ('|' if Ai == Bj else e) + AM
        i -= 1
        j -= 1
    elif i >= 2 and m[i][j] == B:
        AA = Ai + AA
        AB = '-' + AB
        AM = e + AM
        i -= 1
    else:
        AA = '-' + AA
        AB = Bj + AB
        AM = e + AM
        j -= 1

    r1 = i - 1
    r2 = j - 1
    if m[i][j] <= 0:
        break

# Layout & Final adjustment
tM = ''
tS = ''

# Check the end.
AA += s0[x - 1:n_0 - x]
AB += s1[y - 1:n_1 - y]

# Check the beginning.
AA = s0[:r1] + AA
AB = s1[:r2] + AB

if r1 > r2:
    v = r1 - r2
    AB = (e * v) + AB
    AM = (e * (v + r2)) + AM
else:
    v = r2 - r1
    AA = (e * v) + AA
    AM = (e * (v + r1)) + AM

# Print the alignment.
print(AA)
print(AM)
print(AB)
"""

"""
import tkinter as tk
import requests


def citeste():
    url = 'https://www.springer.com'

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        print(html_content)
    else:
        print("Failed to retrieve the webpage")

    # -------------------------
    # VERSION 2: GET with params
    # -------------------------
    url = 'https://springer.com/api'

    params = {
        'param1': 'value1',
        'param2': 'value2'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print(response.text)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
    text = response.text
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, text)


root = tk.Tk()
root.geometry("500x300")

btn = tk.Button(root, text="Citeste fisier", command=citeste)
btn.place(x=150, y=20, width=200, height=40)

# Textbox
textbox = tk.Text(root)
textbox.place(x=50, y=80, width=350, height=180)

# Scrollbar vertical
scroll = tk.Scrollbar(root, command=textbox.yview)
scroll.place(x=400, y=80, height=180)

# Legătură Text « Scroll
textbox.config(yscrollcommand=scroll.set)

root.mainloop()
"""
"""
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y=[10,14,13,18,20]

plt.plot(x,y)
plt.show()
plt.title('Titlu plot')
"""

"""
import matplotlib.pyplot as plt

luni = ["Ian","Feb","Mar","Apr","Mai"]
vanzari = [100,120,115,140,160]

plt.plot(luni,vanzari)
plt.xlabel('Luna')
plt.ylabel('Vanzari')
plt.title('Vanzari pe luni')
plt.show()
"""
"""
import matplotlib.pyplot as plt

regiuni = ["Nord","Sud","Est","Vest"]
clienti = [25,18,32,20]

plt.bar(regiuni,clienti)
plt.xlabel('regiune')
plt.ylabel('clienti')
plt.title('Clienti pe regiune')
plt.show()
"""
"""
import matplotlib.pyplot as plt

varste = [21,22,22,23,24,24,25,26,27,29,30,31,35]

plt.hist(varste,bins=5)
plt.xlabel("Varsta")
plt.ylabel("Frecventa")
plt.title("Distributia varstelor")
plt.show()
"""

"""
import matplotlib.pyplot as plt

varsta = [20,22,25,27,30,35,40]
venit = [2500,2700,3200,3400,4000,4600,5200]

plt.scatter(varsta,venit)
plt.xlabel("Varsta")
plt.ylabel("Venit")
plt.title("Varsta vs Venit")
plt.show()
"""
"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("vanzari.csv")

plt.plot(df['luna'],df['vanzari'],df['target'])
plt.xlabel('Luna')
plt.ylabel('Vanzari')
plt.title('Vanzari pe luna')
plt.show()
"""

"""Cerinta:
Folositi Spectra Forecast. Semnalul A va fi reprezentat de coloana "Vanzari" iar semnalul B va fi reprezentat de coloana "Target". Plotati semnalul M pentru d= 50

"""

"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("vanzari.csv")

A = df['vanzari']
B = df['target']

M = (A - B).rolling(window=50).mean()  # d = 50

plt.plot(df['luna'], A, label='Vanzari (A)')
plt.plot(df['luna'], B, label='Target (B)')
plt.plot(df['luna'], M, label='Semnal M (d=50)', linewidth=2)

plt.xlabel('Luna')
plt.ylabel('Valori')
plt.title('Spectra Forecast - d=50')
plt.legend()
plt.show()
"""

"""
# Frecventa pe litere intr un site

import tkinter as tk
import requests
from collections import Counter
import string

def frecventa_litere(text):
    text = text.lower()

    # păstrăm doar literele
    litere = [c for c in text if c in string.ascii_lowercase]

    return Counter(litere)

def citeste():
    url = 'https://www.springer.com'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text

        # frecvența literelor
        freq = frecventa_litere(html_content)

        # sortare descrescătoare
        rezultat = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # afișare în textbox
        textbox.delete("1.0", tk.END)

        for litera, nr in rezultat:
            textbox.insert(tk.END, f"{litera} : {nr}\n")

    else:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "Failed to retrieve the webpage")

root = tk.Tk()
root.geometry("500x300")

btn = tk.Button(root, text="Citeste si frecventa litere", command=citeste)
btn.place(x=150, y=20, width=200, height=40)

textbox = tk.Text(root)
textbox.place(x=50, y=80, width=350, height=180)

scroll = tk.Scrollbar(root, command=textbox.yview)
scroll.place(x=400, y=80, height=180)

textbox.config(yscrollcommand=scroll.set)

root.mainloop()
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def deseneaza_plot ():
    ax.clear()
    ax.plot(x, y)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Line plot")
    canvas.draw()

x = [1, 2, 3, 4, 5]
y = [10, 14, 13, 18, 20]

root = tk.Tk()
root.title("Plot in aceeasi fereastra")
root.geometry("700x500")

buton = tk.Button(root, text="Afiseaza plot", command=deseneaza_plot)
buton.pack (pady=10)

fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop ()