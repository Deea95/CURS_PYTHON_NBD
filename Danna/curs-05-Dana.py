# # Scriere json
#
# import json
#
# student = {
#     "nume": "Popescu",
#     "varsta": 21,
#     "note": [9, 10, 8]
#
# }
#
# with open("student.json", "w") as f:
#     json.dump(student, f)
from itertools import count

# # Citire json
#
# import json
#
# with open("student.json", "r") as f:
#     data = json. load(f)
#
# print(data["nume"])
# print(data["note"])


# # Exemplu combinat ( JSON + procesare)
# import json
#
# with open("student.json", "r") as f:
#     data = json. load(f)
#
# media = sum(data["note"]) / len(data["note"])
# print("Media:", media)


# # Excel citire, scriere, manipulare ( de testat :
# #    nume   nota
# # 0  Ana    10
# # 1  Ion    8)
# import pandas as pd
#
# # creare tabel
# df = pd. DataFrame ({
#     "nume": ["Ana", "Ion"],
#     "nota": [9, 7]
# })
#
# # salvare Excel
# df.to_excel("note.xlsx", index=False)
#
# # citire Excel
# df2 = pd.read_excel("note.xlsx")
#
# # manipulare
# df2["nota"] = df2["nota"] + 1
#
# print(df2)


# # Generare date random + fișiere mari
# import random
#
# with open("date_mari.txt", "w") as f:
#     for i in range(100000): # fisier mare
#         numar = random.randint(1, 1000)
#         f.write(str(numar) + "\n")


# # Procesare fara a incarca tot in memorie
# total = 0
# count = 0
#
# with open("date_mari.txt", "r") as f:
#     for linie in f:
#         total += int(linie)
#         count += 1
#
# if count > 0:
#     media = total / count
#     print(media)
# else:
#     print("Fisierul este gol")
#
# #print(total)




# # root = fereastra principala a aplicatiei
# # tk.Entry(root) =  creeaza un camp de text in fereastra root
# # entry(pack) = spune unde sa fie pus (il afiseaza in fereastra)
# # Entry = input
# # root = unde apare
# # pack() = il face vizibil
#
#
# import tkinter as tk
# import random
#
# def afiseaza():
#     text = entry.get()
#     with open("test.txt", "w") as f:
#         for i in range(int(text)):
#             numar = random.randint(1, 10)
#             f.write(str(numar) + "\n")
#
#     # fisier mare
#
# root = tk.Tk()
# root.title("Exemplu GUI")
#
# entry = tk.Entry(root)
# entry.pack()
#
# buton = tk.Button(root, text="Apasa", command=afiseaza)
# buton.pack()
#
# label = tk.Label(root, text="")
# label.pack()
#
# root.mainloop()




# # x,y -> pozitie
# # width, height -> dimensiune
# # geometry() -> dimensiunea ferestrei
#
# import tkinter as tk
#
# def afiseaza():
#     text = entry.get()
#     label.config(text="Ai scris: " + text)
#
# root = tk.Tk()
# root.title("Exemplu GUI")
# root.geometry("400x250") # dimensiune fereastră
#
# # Input
# entry = tk. Entry(root)
# entry.place(x=100, y=100, width=200, height=30)
#
# # Buton
# buton = tk.Button(root, text="Apasa", command=afiseaza)
# buton.place(x=150, y=40, width=100, height=40)
#
# # Label rezultat
# label = tk.Label(root, text="")
# label.place(x=100, y=150, width=200, height=30)
#
# root.mainloop( )



# # introduc 2 numere si butonul "+" va afisa suma celor 2 nrumere
#
# import tkinter as tk
#
# def calc():
#     a = int(e1.get())
#     b = int(e2.get())
#     rez.config(text=str(a+b))
#
# root = tk.Tk()
# root.geometry("300x200")
#
# e1 = tk.Entry(root)
# e1.place(x=50, y=30, width=80)
#
# e2 = tk.Entry(root)
# e2.place(x=170, y=30, width=80)
#
# btn = tk.Button(root, text="+", command=calc)
# btn.place(x=120, y=70, width=60, height=30)
#
# rez = tk.Label(root, text="")
# rez.place(x=100, y=120, width=100, height=30)
#
# root.mainloop()



# # 2 butoane care modifica fundalul in rosu sau verde
#
# import tkinter as tk
#
# def rosu():
#     root.config(bg="#cc182e")   # sau root.config(bg="red")
#
# def verde():
#     root.config(bg="#2fc70d")   # sau root.config(bg="green")
#
# root = tk.Tk()
# root.geometry("300x200")
#
# b1 = tk.Button(root, text="Rosu", command=rosu)
# b1.place(x=50, y=80, width=80, height=40)
#
# b2 = tk.Button(root, text="Verde", command=verde)
# b2.place(x=170, y=80, width=80, height=40)
#
# root.mainloop()




# # Verificare parola. Daca parola e gresita => background rosu,
# #                iar daca parola e corecta => background verde
# # Butonul "Apasa" l-am facut sa nu se mai apese prin click, ci prin enter
#
# import tkinter as tk
#
# def verifica():
#     if entry.get() == "1234":
#         label.config(text="Corect")
#         root.config(bg="#2fc70d")
#     else:
#         label.config(text="Gresit")
#         root.config(bg="#cc182e")
#
# root = tk.Tk()
# root.geometry("300x200")
#
# entry = tk. Entry(root, show="*")
# entry.place(x=80, y=40, width=140)
#
# root.bind("<Return>", lambda event: verifica())
#
# btn = tk.Button(root, text="Check", command=verifica)
# btn.place(x=100, y=80, width=100, height=30)
#
# label = tk.Label(root, text="")
# label.place(x=100, y=130, width=100)
#
# root.mainloop()



# # citeste fisier
# import tkinter as tk
#
# def citeste():
#     with open(r"C:\Users\DanielaOancea\OneDrive - New Business Dimensions\Desktop\NBD\curs Python\CURS_PYTHON_NBD\Danna\date_mari.txt", "r") as f:
#         text = f.read()
#     label.config(text=text[:50])
#
# root = tk.Tk()
# root.geometry("400x200")
#
# btn = tk.Button(root, text="Citeste fisier", command=citeste)
# btn.place(x=120, y=40, width=150, height=40)
#
# label = tk.Label(root, text="")
# label.place(x=50, y=120, width=300, height=40)
#
# root.mainloop()



# # citeste fisierul si e aduce continutul fisierului
#
# import tkinter as tk
#
# def citeste():
#     with open(r"C:\Users\DanielaOancea\OneDrive - New Business Dimensions\Desktop\NBD\curs Python\CURS_PYTHON_NBD\Danna\date_mari.txt", "r") as f:
#         text = f.read()
#     textbox.delete("1.0", tk.END)
#     textbox.insert(tk.END, text)
#
# root = tk. Tk()
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
# # Legătură Text Scroll
# textbox.config(yscrollcommand=scroll.set)
#
# root.mainloop()



# # Smooth signal
#
# def smooth(a):
#     n = len(a)
#     for i in range(1, n - 1):
#         a[i] = (a[i - 1] + a[i + 1]) / 2
#     return (a)
#
#
# a = [5, 1, 8, 4, 6, 2, 9, 8]
# print(smooth(a))



# # Afisati in text box rezultatul de la ex de mai sus, dupa ce introduci parola corecta
#
# import tkinter as tk
#
# def smooth(a):
#     n = len(a)
#     b = a.copy()  # copie ca să nu stricăm valorile originale
#     for i in range(1, n - 1):
#         b[i] = (a[i - 1] + a[i + 1]) / 2
#     return b
#
#
# def verifica():
#     if entry.get() == "1234":
#         root.config(bg="green")
#         label.config(text="Corect")
#
#         a = [5, 1, 8, 4, 6, 2, 9, 8]
#         rezultat = smooth(a)
#
#         textbox.delete("1.0", tk.END)
#         textbox.insert(tk.END, str(rezultat))
#
#     else:
#         root.config(bg="red")
#         label.config(text="Gresit")
#
#         a = []
#         rezultat = smooth(a)
#
#         textbox.delete("1.0", tk.END)
#         textbox.insert(tk.END, str(rezultat))
#
#
# root = tk.Tk()
# root.geometry("350x300")
#
# entry = tk.Entry(root, show="*")
# entry.place(x=100, y=20, width=140)
#
# btn = tk.Button(root, text="Check", command=verifica)
# btn.place(x=120, y=60, width=100, height=30)
#
# label = tk.Label(root, text="")
# label.place(x=120, y=100, width=100)
#
# textbox = tk.Text(root, height=5, width=30)
# textbox.place(x=60, y=140)
#
# root.mainloop()


# # ALPHABET DETECTION. ( in exemplu, se scriu intr-o lista, o singura data, literele care se regasesc de mai multe ori in text)
#
# def alpha(c):
#     a = []
#     t = list(c)
#     k = len(t)
#
#     for i in range(k):
#         q = 1
#         for j in range(len(a)):
#             if t[i] == a[j]:
#                 q = 0
#         if q == 1:
#             a.append(t[i])
#     return a
#
# print(alpha('uiuhd87wqsaidhsad'))


# # exemplu cu matrice pt exercitiul de mai sus
# c = [
#     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
#     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
#     [0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
#     [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
#     [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
#     [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
# ]
#
#
# def matrix_alphabet(t):
#     a = []
#     n = len(t)
#     m = len(t[0])
#     for i in range(n):
#         for j in range(m):
#             q = 1
#             for k in range(len(a) + 1):
#                 if k < len(a) and t[i][j] == a[k]:
#                     q = 0
#             if q == 1:
#                 a.append(t[i][j])
#     return a
# print(matrix_alphabet(c))




# # Inside the loop, it assigns the value of b[i] t the number of elements), and stores it in the
# # that value to b[r] and increments the value ranges and is written for this book.To my
#
# a = {}
# b = [3, 6, 2, 78, 99, 1, 4]
#
# r = 0
# n = len(b)
#
# for i in range(n):
#     a[b[i]] = b[i]
#
# m = max(a.keys()) + 1
#
# for j in range(m):
#     if j in a:
#         b[r] = a[j]
#         r += 1
# print(b)



# # Return an array with proportions (relative frequencies)
#
# def p(a):
#     max_value = max(a)
#     n = len(a)
#     m = 100
#
#     # Preaallocate the list
#     # with the required size.
#
#     t = [''] * n
#     for i in range(n):
#         t[i] = str(round((m / max_value) * a[i])) + '%'
#
#     return t
#
# ......nu am apucat sa scriu tot


# Pearson correlation coefficient

def p(a, b):
    n = len(a)
    m = [0, 0]
    for i in range(n):
        m[0] += a[i]
        m[1] += b[i]
    m[0] = m[0] / n  # mean a.
    m[1] = m[1] / n  # mean b.
    s0 = 0
    s1 = 0
    s2 = 0
    for i in range(n):
        s0 += (a[i] - m[0]) * (b[i]-m[1])
        s1 += (a[i] -m[0]) ** 2
        s2 += (b[i] - m[1]) ** 2
    r = s0 / (s1 * s2) ** 0.5
    return r
a = [6, 8, 10]
b = [12, 10, 20]
print(p(a, b))