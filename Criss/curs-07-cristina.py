# #1
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("vanzari.csv")
#
# plt.plot(df["luna"], df["vanzari"])
# plt.xlabel("Luna")
# plt.ylabel("Vanzari")
# plt.title("Vanzari din CSV")
# plt.show()


#2 Graficul e gol si are butonul "Afiseaza plot" pe care daca il apas, imi apare pe axa line chart-ul
# import tkinter as tk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# def deseneaza_plot():
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
# buton = tk. Button(root, text="Afiseaza plot", command=deseneaza_plot)
# buton.pack(pady=10)
#
# fig = Figure(figsize=(6, 4), dpi=100)
# ax = fig.add_subplot(111)
#
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#
# root.mainloop()


#3 Validare input  (e similar cu introducerea parolei)
# import tkinter as tk
# from tkinter import messagebox
#
# def verifica():
#     text = entry.get()
#
#     try:
#          valoare = float(text.replace(",", "."))
#          label_rezultat.config(text=f"Valoare validă: {valoare}")
#     except ValueError:
#          messagebox. showerror("Eroare", "Introduceti un numar valid.")
#
# root = tk. Tk()
# root. title("Validare input")
# root.geometry("300x150")
#
# entry = tk. Entry(root)
# entry.pack(pady=10)
#
# button = tk.Button(root, text="Check", command=verifica)
# button.pack()
#
# label_rezultat = tk. Label(root, text="")
# label_rezultat.pack(pady=10)
#
# root.mainloop()


#4 extragere nume utilizator din email (VAR 1)

# # Citire adresa de email de la tastatură
# email = input("Introdu adresa de email: ")
#
# # Extragere nume utilizator
# username = email.split("@")[0]
#
# # Afișare rezultat
# print("Nume utilizator:", username)
#

#4 VAR 2 cu buton
# import tkinter as tk
# from tkinter import messagebox
#
#
# def verifica_email():
#     text = entry.get()
#
#     try:
#         utilizator = text.split("@")[0]
#
#         label_rezultat.config(
#             text=f"Nume utilizator: {utilizator}"
#         )
#
#     except Exception:
#         messagebox.showerror(
#             "Eroare",
#             "Introduceți un email valid."
#         )
#
# root = tk. Tk()
# root. title("Validare input")
# root.geometry("300x150")
#
# entry = tk. Entry(root)
# entry.pack(pady=10)
#
# button = tk.Button(root, text="Check", command=verifica_email)
# button.pack()
#
# label_rezultat = tk. Label(root, text="")
# label_rezultat.pack(pady=10)
#
# root.mainloop()


#5
# import tkinter as tk
# from tkinter import messagebox
#
# def calculeaza():
#     text = entry.get()
#
#     try:
#         valori = [float(x.strip().replace(",", ".")) for x in text.split(";")]
#         valori_smooth = smooth(valori, 3)
#         label.config(text=str(valori_smooth))
#     except ValueError:
#         messagebox. showerror("Eroare", "Introduceti valori separate prin ;")
#
# def smooth(lista, fereastra=3):
#     rezultat = []
#
#     for i in range(len(lista)):
#         start = max(0, i - fereastra + 1)
#         valori = lista[start: i+1]
#         rezultat.append(sum(valori) / len(valori))
#
#     return rezultat
#
# root = tk. Tk()
# root.geometry("500x200")
# root. title("Smooth numeric")
#
# entry = tk.Entry(root, width=60)
# entry.pack(pady=10)
#
# button = tk. Button(root, text="Calculeaza smooth", command=calculeaza)
# button.pack()
#
# label = tk. Label(root, text="")
# label.pack(pady=10)
#
# root.mainloop()


#6
# Citire CSV mare fără încarcare completă
# Cititi un fișier CSV mare în bucăți și calculați totalul unei coloane.
#
# import pandas as pd
#
# fisier = "date_mari.csv"
# total = 0
#
# for bucata in pd.read_csv(fisier, chunksize=1000):
#     total += bucata["valoare"]. sum()
#
# print("Total:", total)


#7
import pandas as pd

df = pd.read_csv("clienti.csv")
print("Valori lipsa:")
print(df.isna().sum())

print("Duplicate:")
print(df.duplicated().sum())

df_curat = df.dropna()
df_curat = df_curat.drop_duplicates()

print("Dimensiune initiala: ", df.shape)
print("Dimensiune finala: ", df_curat.shape)

df_curat.to_csv("clienti_curatat.csv", index=False)


#8
# import pandas as pd
#
# # Crearea datelor pentru fișierul Excel/CSV
# # Amestecăm clienți unici cu duplicate
# data = [
#     ["Andrei Ionescu", "C001"],
#     ["Maria Georgescu", "C002"],
#     ["Ion Popescu", "C003"],
#     ["Andrei Ionescu", "C001"],  # Duplicat
#     ["Elena Dumitru", "C004"],
#     ["Cristian Vasile", "C005"],
#     ["Maria Georgescu", "C002"],  # Duplicat
#     ["Stefan Radu", "C006"],
#     ["Ioana Stoica", "C007"],
#     ["Ion Popescu", "C003"],      # Duplicat
#     ["Andreea Marin", "C008"],
#     ["Matei Enache", "C009"],
#     ["Cristian Vasile", "C005"],  # Duplicat
#     ["Lucian Stan", "C010"],
#     ["Mihaela Popa", "C011"],
#     ["Robert Dobre", "C012"],
#     ["Elena Dumitru", "C004"],    # Duplicat
#     ["Gabriel Neagu", "C013"],
#     ["Simona Iancu", "C014"],
#     ["Andrei Ionescu", "C001"]    # Triplicat
# ]
#
# df = pd.DataFrame(data, columns=["nume", "cod"])
#
# # Salvare ca CSV
# csv_file = "clienti.csv"
# df.to_csv(csv_file, index=False, encoding='utf-8-sig')
#
# # Salvare ca XLSX (pentru un format gata de Excel)
# xlsx_file = "clienti_formatat.xlsx"
# df.to_excel(xlsx_file, index=False)
#
# print(f"Fișiere generate: {csv_file}, {xlsx_file}")


#9
# import pandas as pd
#
# df1 = pd.read_csv("date_mari.csv")
# df2 = pd.read_csv("vanzari.csv")
#
# diferente = df1.merge(df2, how="outer", indicator=True)
# diferente = diferente[diferente["_merge"] != "both"]
#
# print(diferente)
#
# diferente.to_csv("diferente.csv", index=False)


#10
#Raport statistic pe regiuni și tipuri de clienti
# Dintr-un fisier cu produse, regiuni, vârste și tipuri de clienti,
# calculați numarul de produse pe regiune și pe tip de client.

# import pandas as pd
#
# df = pd.read_csv("produse.csv")
#
# raport = df.groupby(["regiune","tip_client"])["produs"].count()
#
# print(raport)
#
# raport.to_excel("raport_static.xlsx")


#11
# import time
# from datetime import datetime
#
# evenimente = [
#     {
#         "titlu": "Raport zilnic",
#         "ora": 12,
#         "minut": 3,
#         "mesaj": "Verifica raportul bancar."
#     }
# ]
# notificat = False
#
# while True:
#
#     acum = datetime.now()
#
#     print("Ora curentă:", acum.strftime("%H:%M:s"))
#
#     for eveniment in evenimente:
#
#         if (
#             acum. hour == eveniment["ora"] and
#             acum.minute == eveniment["minut"] and
#             notificat == False
#         ):
#             print("NOTIFICARE")
#             print(eveniment["titlu"])
#             print(eveniment["mesaj"])
#
#             notificat = True
#
#     if acum.minute != evenimente[0]["minut"]:
#         notificat = False
#
#     time.sleep(1)


#12 count down
import time
from datetime import datetime, timedelta

evenimente = [
    {
        "titlu": "Raport zilnic",
        "ora": 12,
        "minut": 30,
        "mesaj": "Verifică raportul bancar."
    }
]

notificat = False

while True:

    acum = datetime.now()

    tinta = acum.replace(
        hour=evenimente[0]["ora"],
        minute=evenimente[0]["minut"],
        second=0,
        microsecond=0
    )
    if tinta < acum:
        tinta = tinta + timedelta(days=1)

    diferenta = tinta - acum

    # elimină miimile / microsecundele
    diferenta = diferenta - timedelta(microseconds=diferenta.microseconds)

    print("Timp rămas până la notificare:", diferenta)

    for eveniment in evenimente:

        if (
                acum.hour == eveniment["ora"] and
                acum.minute == eveniment["minut"] and
                notificat == False

        ):
            print("NOTIFICARE")
            print(eveniment["titlu"])
            print(eveniment["mesaj"])

            notificat = True

    if acum.minute != evenimente[0]["minut"]:
        notificat = False

    time.sleep(1)
