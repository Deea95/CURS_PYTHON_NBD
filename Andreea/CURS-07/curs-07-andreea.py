# Ex 1
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vanzari.csv")
plt.plot(df['luna'],df['vanzari'])
plt.xlabel("luna")
plt.ylabel("vanzari")
plt.title("vanzari din CSV")
plt.show()
"""
"""
import tkinter as tk
from matplotlib. figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def deseneaza_plot():
    ax.clear()
    ax.plot(x, y)
    ax.set_xlabel("Axa X")
    ax. set_ylabel("Y")
    ax. set_title("Line plot")
    canvas. draw()

x = [1, 2, 3, 4, 5]
y = [10, 14, 13, 18, 20]

root = tk. Tk()
root. title("Plot in aceeasi fereastra")
root.geometry("700x500")

buton = tk. Button(root, text="Afiseaza plot", command=deseneaza_plot)
buton .pack (pady=10)

fig = Figure(figsize=(6, 4), dpi=100)
ax = fig. add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()
"""
# Validare input (Exemplu):
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

# Citeste fisiere csv ff mari
# import pandas as pd
#
# fisier = "vanzari.csv"
# total = 0
#
# for bucata in pd.read_csv(fisier, chunksize=1000):
#     total += bucata['vanzari'].sum()
#
# print("Total:", total)

#Verificare date lipsa si duplicate:
# import pandas as pd
#
# df = pd.read_csv("clienti.csv")
# print("Valori lipsa:")
# print(df.isna().sum())
#
# print("Duplicate:")
# print(df.duplicated().sum())
#
# df_curat = df.dropna()
# df_curat = df_curat.drop_duplicates()
#
# print("Dimensiune initiala: ", df.shape)
# print("Dimensiune finala: ", df_curat.shape)
#
# df_curat.to_csv("clienti_curatat.csv", index=False)

# sau
#
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

# comparare intre 2 fisiere CSV; Comparati 2 fisiere CSV si afisati liniile care exista in primul
# dar nu exista si n al doilea
# import pandas as pd
#
# # 1. Încarcă cele două fișiere
# df1 = pd.read_csv('clienti.csv')
# df2 = pd.read_csv('clienti_curatat.csv')
#
# # 2. Identifică liniile care sunt în df1 dar NU și în df2
# # Folosim un "left join" cu indicator pentru a vedea sursa fiecărui rând
# comparatie = df1.merge(df2, how='left', indicator=True)
#
# # 3. Filtrăm doar rândurile care apar exclusiv în primul fișier ('left_only')
# doar_in_primul = comparatie[comparatie['_merge'] == 'left_only'].drop(columns=['_merge'])
#
# # 4. Afișează rezultatul sau salvează-l
# print("Linii care există doar în primul fișier:")
# print(doar_in_primul)
#
# # Salvare opțională
# # doar_in_primul.to_csv('rezultat_comparare.csv', index=False)

# import pandas as pd
#
# df1 = pd.read_csv("clienti_curatat.csv")
# df2 = pd.read_csv("clienti.csv")
#
# diferente = df1.merge(df2, how="outer", indicator=True)
# diferente = diferente[diferente["_merge"] != "both" ]
#
# print(diferente)
#
# diferente.to_csv("diferente.csv", index=False)

#
# import pandas as pd
#
# df = pd.read_csv("produse.csv")
#
# raport = df.groupby(["regiune","tip_client"])["produs"].count()
#
# print(raport)
#
# raport.to_excel("raport_static.xlsx")

# Event Notifier simplificat

# import time
# from datetime import datetime, timedelta
#
# # Setăm evenimentul să aibă loc chiar în minutul curent pentru test
# acum_init = datetime.now()
# minut_test = acum_init.minute
# ora_test = acum_init.hour
#
# evenimente = [
#     {
#         "titlu": "Test Rapid",
#         "ora": ora_test,
#         "minut": minut_test,
#         "mesaj": "Notificarea de test a funcționat!"
#     }
# ]
#
# notificat = False
# timp_start = time.time()
#
# print(f"Programul rulează pentru 1 minut (Țintă: {ora_test:02d}:{minut_test:02d})...")
#
# # Rulează timp de 60 de secunde
# while time.time() - timp_start < 60:
#     acum = datetime.now()
#
#     # Afișare ceas în consolă pe același rând
#     print(f"Ora: {acum.strftime('%H:%M:%S')}", end="\r")
#
#     for eveniment in evenimente:
#         # Verificăm ora, minutul și dacă nu a fost deja trimisă notificarea
#         if (acum.hour == eveniment["ora"] and
#                 acum.minute == eveniment["minut"] and
#                 not notificat):
#             print("\n\n🔔 [NOTIFICARE ACTIVĂ]")
#             print(f"SUBIECT: {eveniment['titlu']}")
#             print(f"MESAJ: {eveniment['mesaj']}")
#             print("-" * 20 + "\n")
#
#             notificat = True
#
#     # Resetăm starea dacă minutul s-a schimbat (pentru a permite alerte viitoare)
#     if acum.minute != minut_test:
#         notificat = False
#
#     time.sleep(1)
#
# print("\n\nTest încheiat după 60 de secunde.")

# # Countdown:
# import time
# from datetime import datetime
# import sys
#
# # --- DATELE COLEGILOR (Editezi direct aici) ---
# colegi = [
#     {"nume": "Andrei Ionescu", "data": "1990-05-7"},
#     {"nume": "Maria Georgescu", "data": "1992-10-20"},
#     {"nume": "Ion Popescu", "data": "1985-05-07"},  # Am pus 8 Mai pentru test
#     {"nume": "Elena Dumitru", "data": "1995-12-01"},
# ]
#
#
# def gaseste_urmatoarea_aniversare():
#     acum = datetime.now()
#     viitoare = []
#
#     for c in colegi:
#         data_n = datetime.strptime(c["data"], "%Y-%m-%d")
#         # Setăm ziua aniversară în anul curent
#         aniv_anul_asta = data_n.replace(year=acum.year, hour=0, minute=0, second=0)
#
#         # Dacă a trecut deja, setăm pentru anul viitor
#         if aniv_anul_asta < acum:
#             aniv_anul_asta = aniv_anul_asta.replace(year=acum.year + 1)
#
#         viitoare.append({"nume": c["nume"], "data": aniv_anul_asta})
#
#     # Sortăm după data cea mai apropiată
#     return sorted(viitoare, key=lambda x: x["data"])[0]
#
#
# def artificii():
#     print("\n" + " " * 15 + "✨ ✨ ✨ ✨ ✨")
#     print(" " * 10 + "🎉 LA MULȚI ANI! 🎉")
#     print(" " * 15 + "✨ ✨ ✨ ✨ ✨\n")
#
#
# def porneste_countdown():
#     urmator = gaseste_urmatoarea_aniversare()
#     tinta = urmator["data"]
#     nume = urmator["nume"]
#
#     print(f"🚀 Sistem pornit. Următoarea petrecere: {nume} ({tinta.strftime('%d %B')})")
#     print("Apasă Ctrl+C pentru a opri.\n")
#
#     try:
#         while True:
#             acum = datetime.now()
#             dif = tinta - acum
#
#             if dif.total_seconds() <= 0:
#                 artificii()
#                 break
#
#             # Formatăm countdown-ul
#             zile = dif.days
#             ore, rest = divmod(dif.seconds, 3600)
#             minute, secunde = divmod(rest, 60)
#
#             # Efect de "typing" pe același rând
#             sys.stdout.write(
#                 f"\r⏳ Timp rămas până la ziua lui {nume}: "
#                 f"{zile}z {ore:02d}h {minute:02d}m {secunde:02d}s "
#             )
#             sys.stdout.flush()
#             time.sleep(1)
#
#     except KeyboardInterrupt:
#         print("\n\nSistem oprit. Ne vedem la următoarea felie de tort! 🍰")
#
#
# if __name__ == "__main__":
#     porneste_countdown()

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --- DATELE COLEGILOR ---
colegi = [
    {"nume": "Andrei Ionescu", "data": "1990-05-15"},
    {"nume": "Maria Georgescu", "data": "1992-10-20"},
    {"nume": "Ion Popescu", "data": "1985-05-08"},
    {"nume": "Elena Dumitru", "data": "1995-12-01"},
    {"nume": "Test Coleg", "data": "1990-05-07"}  # Azi pentru test
]


class BirthdayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NBD Birthday Dashboard")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")

        # Titlu
        self.label_titlu = tk.Label(root, text="🎉 Următoarea Aniversare 🎉",
                                    font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
        self.label_titlu.pack(pady=20)

        # Numele sărbătoritului
        self.label_nume = tk.Label(root, text="", font=("Helvetica", 24), bg="#2c3e50", fg="#f1c40f")
        self.label_nume.pack()

        # Countdown
        self.label_timer = tk.Label(root, text="", font=("Courier New", 20), bg="#2c3e50", fg="#e74c3c")
        self.label_timer.pack(pady=20)

        # Listă restul colegilor
        self.lista_frame = tk.Frame(root, bg="#34495e", padx=10, pady=10)
        self.lista_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.label_lista = tk.Label(self.lista_frame, text="Calendarul lunii:",
                                    bg="#34495e", fg="#bdc3c7", font=("Helvetica", 10, "italic"))
        self.label_lista.pack(anchor="w")

        self.update_timer()

    def gaseste_eveniment(self):
        acum = datetime.now()
        viitoare = []
        for c in colegi:
            dn = datetime.strptime(c["data"], "%Y-%m-%d")
            aniv = dn.replace(year=acum.year, hour=0, minute=0, second=0)
            if aniv < acum.replace(hour=0, minute=0, second=0):
                aniv = aniv.replace(year=acum.year + 1)
            viitoare.append({"nume": c["nume"], "data": aniv})
        return sorted(viitoare, key=lambda x: x["data"])[0]

    def update_timer(self):
        eveniment = self.gaseste_eveniment()
        tinta = eveniment["data"]
        acum = datetime.now()
        dif = tinta - acum

        self.label_nume.config(text=eveniment["nume"])

        if dif.total_seconds() <= 0:
            self.label_timer.config(text="ESTE ZIUA LUI! 🎂", fg="#2ecc71")
        else:
            zile = dif.days
            ore, rest = divmod(dif.seconds, 3600)
            minut, sec = divmod(rest, 60)
            self.label_timer.config(text=f"{zile}z {ore:02d}h {minut:02d}m {sec:02d}s")

        # Refresh la fiecare secundă
        self.root.after(1000, self.update_timer)


# Pornire Aplicație
root = tk.Tk()
app = BirthdayApp(root)
root.mainloop()