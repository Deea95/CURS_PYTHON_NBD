# # crearea fisierului - scriere din json
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
#
#
# # Citire json
#
# import json
#
# with open("student.json", "r") as f:
#     data = json. load(f)
#
# print(data["nume"])
# print(data["note"])
#
# #exemplu combinat (json +procesare)
# import json
#
# with open("student.json", "r") as f:
#     data = json. load(f)
#
# media = sum(data["note"]) / len(data["note"])
# print("Media:", media)
#
#
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
#
#
#
# #Generare date random + fișiere mari
# import random
#
# with open("date_mari.txt", "w") as f:
#     for i in range(100000): # fisier mare
#         numar = random.randint(1, 1000)
#         f.write(str(numar) + "\n")
#
#
#
# #procesare fara a incarca tot in memorie
# total = 0
#
# with open("date_mari.txt", "r") as f:
#     for linie in f:
#         total += int(linie)
#
# print(total)
#
#
# #media
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
#

# root = ferestra principala a aplicatiei
# tk.Entry= creeaza un camp de text in fereastra root
# entry.pack() =  spune unde sa fie pus (il afiseaza in fereastra)
# Entry = input
# root = unde apare
# pack = il face vizibil

# import random
# import tkinter as tk
#
# def afiseaza():
#     text = entry.get()
#     with open("date_mari.txt", "w") as f:
#         for i in range(100000):  # fișier mare
#             numar = random.randint(1, 1000)
#             f.write(str(numar) + "\n")
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


# x,y -> pozitie
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
# # Buton
# buton = tk.Button(root, text="Apasa", command=afiseaza)
# buton.place(x=150, y=40, width=100, height=30)
#
# # Input
# entry = tk. Entry(root)
# entry.place(x=100, y=100, width=200, height=30)
#
# # Label rezultat
# label = tk.Label(root, text="")
# label.place(x=100, y=150, width=200, height=30)
#
# root.mainloop()
#

# #calculator
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


# import tkinter as tk
#
#
# def rosu():
#     root.config(bg="#cc182e")  # root.config(bg="red")
#
#
# def verde():
#     root.config(bg="#2fc70d")
#
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


# # Verificare parola
#
# import tkinter as tk
#
# def verifica():
#     if entry.get() == "1234":
#         label.config(text="Corect")
#     else:
#         label.config(text="Gresit")
#
# root = tk.Tk()
# root.geometry("300x200")
#
# entry = tk. Entry(root, show="*")
# entry.place(x=80, y=40, width=140)
#
# btn = tk.Button(root, text="Check", command=verifica)
# btn.place(x=100, y=80, width=100, height=30)
#
# label = tk.Label(root, text="")
# label.place(x=100, y=130, width=100)
#
# root.mainloop()

# #daca parola este gresita, modificati background-ul in rosu
# import tkinter as tk
#
# def verifica():
#     if entry.get() == "1234":
#         label.config(text="Corect")
#         root.config(bg="green")   # fundal verde
#     else:
#         label.config(text="Gresit")
#         root.config(bg="red")     # fundal rosu
#
# root = tk.Tk()
# root.geometry("300x200")
#
# entry = tk.Entry(root, show="*")
# entry.place(x=80, y=40, width=140)
#
# btn = tk.Button(root, text="Check", command=verifica)
# btn.place(x=100, y=80, width=100, height=30)
#
# label = tk.Label(root, text="")
# label.place(x=100, y=130, width=100)
#
# root.mainloop()
#
#
# #citire fisier text
#
# import tkinter as tk
#
# def citeste():
#     with open(r"C:\Users\CristinaOancea\Desktop\CRISTINA\Python\CURS_PYTHON_NBD\Criss\date_mari.txt", "r") as f:
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

# #ne aduce continutul fisierului
# import tkinter as tk
#
# def citeste():
#     with open(r"C:\Users\CristinaOancea\Desktop\CRISTINA\Python\CURS_PYTHON_NBD\Criss\date_mari.txt", "r") as f:
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
# # Legătură Text # Scroll
# textbox.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# # ex 183 (smooth signal) combinat cu ferestre  (ex de mai sus) cu introducere parola
# import tkinter as tk
#
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


# # ex 183 (smooth signal) combinat cu ferestre  (ex de mai sus) fara introducere parola
# import tkinter as tk
#
# def smooth(a):
#     n = len(a)
#     b = a.copy()
#     for i in range(1, n - 1):
#         b[i] = (a[i - 1] + a[i + 1]) / 2
#     return b
#
#
# def calculeaza():
#     a = [5, 1, 8, 4, 6, 2, 9, 8]
#     rezultat = smooth(a)
#
#     textbox.delete("1.0", tk.END)
#     textbox.insert(tk.END, str(rezultat))
#
#
# root = tk.Tk()
# root.geometry("350x250")
#
# btn = tk.Button(root, text="Calculeaza", command=calculeaza)
# btn.place(x=120, y=40, width=100, height=30)
#
# textbox = tk.Text(root, height=6, width=30)
# textbox.place(x=60, y=100)
#
# root.mainloop()


# ALPHABET DETECTION: adauga in output litera in mod unic din sirul de caractere
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