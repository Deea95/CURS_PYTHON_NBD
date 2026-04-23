# # 10.7.6 Ex. (199) – Shannon entropy
# import math
#
# def entropy(c):
#     a = alpha(c)
#     n = len(a)
#     k = len(c)
#     e = 0
#
#     for i in range(n):
#         r = len(c.replace(a[i], ''))
#         a[i] = (k - r) / k
#         # e += -a[i] * log(2, a[i])
#         e += a[i] * log(2, 1 / a[i])
#     return e
# # ALPHABET DETECTION.
# def alpha(c):
#     a = []
#     t = list(c)
#     k = len(t)
#     for i in range(k):
#         q = 1
#         for j in range(len(a)):
#             if t[i] == a[j]:
#                 q = 0
#         if q == 1:
#             a.append(t[i])
#     return a
#
# def log(n, v):
#     return math.log(v) / math.log(n)
#
#
# print(entropy('uiuhd87wqsaidhsad'))


# # 11.1.1 Ex. (207) – Spectral forecast for signals in Python.
#
# # Spectral forecast for signals in Python.
#
# A = '10.3,23.4,44.8,63.2,44.1,35.1,46.5,62.6,50.4'
# B = '18.8,43.1,52.2,45.5,46.8,46.6,67.9,66.3,70.4'
# M = ''
#
# tA = A.split(',')
# tB = B.split(',')
#
# maxA = max(map(float, tA))
# maxB = max(map(float, tB))
# max_value = max(maxA, maxB)
#
# d = 33
#
# for i in range(len(tA)):
#     v=((d/maxA)*float(tA[i]))+(((max_value-d)/maxB)*float(tB[i]))
#     M += '{:.2f}'.format(v)
#     if i < len(tA)-1:
#         M += ','
# print('Signal A:' + A)
# print('Max(A[i]):' + str(maxA))
# print('Signal M:' + M)
# print('Signal B:' + B)
# print('Max(B[i]):' + str(maxB))


# # 11.1.4 Ex. (210) – Decompose a matrix into multiple matrices based on unique values
# def matrix_alphabet(t):
#     a = []
#     n = len(t)
#     m = len(t[0])
#
#     for i in range(n):
#         for j in range(m):
#             q = 1
#             for k in range(len(a) + 1):
#                 if k < len(a) and t[i][j] == a[k]:
#                     q = 0
#             if q == 1:
#                 a.append(t[i][j])
#     return a
#
#
# def decompose(c, a):
#     n = len(c)
#     m = len(c[0])
#     d = []
#
#     for i in range(n):
#         d.append([])
#         for j in range(m):
#             d[i].append([])
#             for k in range(len(a) + 1):
#                 d [i][j].append(" ")  # "\u2591"
#                 if k < len(a) and c[i][j] == a[k]:
#                     d[i][j][k] = c[i][j]
#     return d
#     return d
#
#
# def SMC(m, k):
#     r = 'M' + str(k + 1)
#     r += '\n ----------\n'
#     for i in range(len(m)):
#         r += "|"
#         for j in range(len(m[i])):
#             r += str(m[i][j][k])
#         r += "|\n"
#     r += ' ----------'
#     return r
#
# # Main code
# r = "u"
# c= [
# [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
# [1, 2, 1, 0, 1, 3, 1, 0, 1, 1],
# [1, 1, 2, 0, 1, 3, 0, 1, 0, 1],
# [0, 1, 0, 2, 1, 3, 1, 0, 0, 1],
# [1, 1, 1, 0, 2, 3, 1, 0, 1, 0],
# [1, 0, 1, 1, 1, 3, 0, r, 0, 0],
# [1, 0, 3, 3, 3, 3, r, 0, 0, 1],
# [1, 0, 1, 1, 1, r, 0, 9, 9, 9],
# [1, 1, 0, 0, 0, 0, 1, 9, 0, 9]
#     ]
#
# b = matrix_alphabet(c)
# t = decompose(c, b)
#
# for k in range(len(b)):
#     print(SMC(t, k))
#
# print(b)



# # 11.1.5 Ex. (211) – Count islands over the matrix and show their location
# a =  [
#     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
#     [1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
#     [1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
# ]
#
# b =  [
#     [+1, 0],  # right side element.
#     [-1, 0],  # left side element.
#     [0, +1],  # upward side element.
#     [0, -1],  # downward side element.
#     [+1, +1], # upward-right side element.
#     [-1, -1], # downward-left side element.
#     [+1, -1], # downward-right side element.
#     [-1, +1]  # upward-left side element.
#     ]
#
# def d(a, i, j, n, m, c):
#     if i < 0 or j < 0 or i > (n - 1) or \
#             j > (m - 1) or a[i][j] != 1:
#             return
#     if a[i][j] == 1:
#         a[i][j] = c + 1
#
#         for k in range(len(b)):
#             d(a, i + b[k][0], j + b[k][1], n, m, c)
#
#
# def SCAN(a):
#     n = len(a)  # row.
#     m = len(a[0])  # col.
#     c = 0  # islands.
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == 1:
#                 c += 1
#                 d(a, i, j, n, m, c)
#     return c
#
#
# def SMC(m):
#     r = "\n"
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             r += str(m[i][j]) + " "
#         r += "\n"
#     return r
#
#
# print("Islands =", SCAN(a))
# print(SMC(a))




import requests
import tkinter as tk

# # -------------------------
# # VERSION 1: simple GET
# # -------------------------
# url = 'https://www.springer.com'
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     html_content = response.text
#     print(html_content)
# else:
#     print("Failed to retrieve the webpage")
#
#
# # -------------------------
# # VERSION 2: GET with params
# # -------------------------
# url = 'https://springer.com/api'
#
# params = {
#     'param1': 'value1',
#     'param2': 'value2'
# }
#
# response = requests.get(url, params=params)
#
# if response.status_code == 200:
#     print(response.text)
# else:
#     print("Failed to retrieve data. Status code:", response.status_code)
#
#
from http.client import responses



# import tkinter as tk
# import requests
#
#
# def citeste():
#     url = 'https://www.springer.com'
#
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         html_content = response.text
#         print(html_content)
#     else:
#         print("Failed to retrieve the webpage")
#
#     # -------------------------
#     # VERSION 2: GET with params
#     # -------------------------
#     url = 'https://springer.com/api'
#
#     params = {
#         'param1': 'value1',
#         'param2': 'value2'
#     }
#
#     response = requests.get(url, params=params)
#
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print("Failed to retrieve data. Status code:", response.status_code)
#     text = response.text
#     textbox.delete("1.0", tk.END)
#     textbox.insert(tk.END, text)
#
#
# root = tk.Tk()
# root.geometry("500x300")
#
# btn = tk.Button(root, text="Citeste fisier", command=citeste)
# btn.place(x=150, y=20, width=200, height=40)
#
# # Textbox
# textbox = tk.Text(root)
# textbox.place(x=50, y=80, width=350, height=180)
#
# # Scrollbar vertical
# scroll = tk.Scrollbar(root, command=textbox.yview)
# scroll.place(x=400, y=80, height=180)
#
# # Legătură Text « Scroll
# textbox.config(yscrollcommand=scroll.set)
#
# root.mainloop()



# # LINE CHART
# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5]
# y=[10,14,13,18,20]
#
# plt.plot(x,y)
# plt.show()
# plt.title('Titlu plot')


# # LINE CHART + denumirea axelor
# import matplotlib.pyplot as plt
#
# luni = ["Ian","Feb","Mar","Apr","Mai"]
# vanzari = [100,120,115,140,160]
#
# plt.plot(luni,vanzari)
# plt.xlabel('Luna')
# plt.ylabel('Vanzari')
# plt.title('Vanzari pe luni')
# plt.show()



# # LINE CHART
# import matplotlib.pyplot as plt
# luni = ["Ian","Feb","Mar", "Apr","Mai"]
# vz = [100,120,115,140,160]
#
# plt.plot(luni,vz)
# plt.xlabel("Luna")
# plt.xlabel("Vanzari")
# plt.title("Vanzari pe luni")
# plt.show()



# # HISTOGRAMA
# import matplotlib.pyplot as plt
#
# varste = [21,22,23,24,24,25,26,27,29,30,31,35]
#
# plt.hist(varste,bins=5)
# plt.xlabel("Varsta")
# plt.xlabel("Frecventa")
# plt.title("Distributia varstelor")
# plt.show()



# # SCATTER PLOT
# import matplotlib.pyplot as plt
#
# varsta = [20, 22, 25, 27, 30, 35, 40]
# venit = [2500, 2700, 3200, 3400, 4000, 4600, 5200]
#
# plt.scatter(varsta, venit)
# plt.xlabel("Varsta")
# plt.ylabel("Venit")
# plt.title("Varsta versus venit")
# plt.show()



# # citire din fisier csv
# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = pd.read_csv("vanzari.csv")
#
# plt.plot(df['luna'],df['vanzari'])
# plt.xlabel('Luna')
# plt.ylabel('Vanzari')
# plt.title('Vanzari pe luna')
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("vanzari.csv")
#
# plt.plot(df["luna"], df["vanzari"])
# plt.xlabel("Luna")
# plt.ylabel("Vanzari")
# plt.title("Vanzari din CSV")
# plt. show()



# Date din csv. + line plot
# CSV vanzari.csv

# luna, vanzari
# Ian, 100
# Feb, 120
# Mar, 115
# Apr, 140
# May, 140


# # Cerinta:
# # Folositi Spectra Forecast. Semnalul A va fi reprezentat de coloana "Vanzari"
# # iar semnalul B va fi reprezentat de coloana "Target". Plotati semnalul M
# # pentru d= 50
#
# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = pd.read_csv("vanzari.csv")
#
# A = df['vanzari']
# B = df['target']
#
# M = (A - B).rolling(window=50).mean()  # d = 50
#
# plt.plot(df['luna'], A, label='Vanzari (A)')
# plt.plot(df['luna'], B, label='Target (B)')
# plt.plot(df['luna'], M, label='Semnal M (d=50)', linewidth=2)
#
# plt.xlabel('Luna')
# plt.ylabel('Valori')
# plt.title('Spectra Forecast - d=50')
# plt.legend()
# plt.show()



# # Frecventa pe litere intr un site
# import tkinter as tk
# import requests
# from collections import Counter
# import string
#
#
# def frecventa_litere(text):
#     text = text.lower()
#
#     # păstrăm doar literele
#     litere = [c for c in text if c in string.ascii_lowercase]
#
#     return Counter(litere)
#
#
# def citeste():
#     url = 'https://www.springer.com'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         html_content = response.text
#
#         # frecvența literelor
#         freq = frecventa_litere(html_content)
#
#         # sortare descrescătoare
#         rezultat = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#
#         # afișare în textbox
#         textbox.delete("1.0", tk.END)
#
#         for litera, nr in rezultat:
#             textbox.insert(tk.END, f"{litera} : {nr}\n")
#
#     else:
#         textbox.delete("1.0", tk.END)
#         textbox.insert(tk.END, "Failed to retrieve the webpage")
#
#
# root = tk.Tk()
# root.geometry("500x300")
#
# btn = tk.Button(root, text="Citeste si frecventa litere", command=citeste)
# btn.place(x=150, y=20, width=200, height=40)
#
# textbox = tk.Text(root)
# textbox.place(x=50, y=80, width=350, height=180)
#
# scroll = tk.Scrollbar(root, command=textbox.yview)
# scroll.place(x=400, y=80, height=180)
#
# textbox.config(yscrollcommand=scroll.set)
#
# root.mainloop()



# # Buton + grafic in aceeasi interfata
# # Buton care afiseaza graficul. Poate fi folosit pentru a ascunde graficul,
# # iar prin intermediul butonului, sa deschidem graficul in alta fereastra
# import tkinter as tk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# def deseneaza_plot ():
#     ax.clear()
#     ax.plot(x, y)
#     ax.set_xlabel("X")
#     ax.set_ylabel("Y")
#     ax.set_title("Line plot")
#     canvas.draw()
#
# x = [1, 2, 3, 4, 5]
# y = [10, 14, 13, 18, 20]
#
# root = tk.Tk()
# root.title("Plot in aceeasi fereastra")
# root.geometry("700x500")
#
# buton = tk.Button(root, text="Afiseaza plot", command=deseneaza_plot)
# buton.pack (pady=10)
#
# fig = Figure(figsize=(6, 4), dpi=100)
# ax = fig.add_subplot(111)
#
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#
# root.mainloop ()



