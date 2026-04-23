# # ex 1 - line
# import matplotlib.pyplot as plt
# luni = ["Ian","Feb","Mar", "Apr","Mai"]
# vz = [100,120,115,140,160]
#
# plt.plot(luni,vz)
# plt.xlabel("Luna")
# plt.xlabel("Vanzari")
# plt.title("Vanzari pe luni")
# plt.show()


# # ex 2 - bar
# import matplotlib.pyplot as plt
# regiuni = ["Nord","Sud","Est", "Vest"]
# clienti = [25,18,32,20]
#
# plt.bar(regiuni,clienti)
# plt.xlabel("Regiuni")
# plt.xlabel("Nr clienti")
# plt.title("Clienti pe regiuni")
# plt.show()


# # ex 3 - histograma
# import matplotlib.pyplot as plt
#
# varste = [21,22,23,24,24,25,26,27,29,30,31,35]
#
# plt.hist(varste,bins=5)
# plt.xlabel("Varsta")
# plt.xlabel("Frecventa")
# plt.title("Distributia varstelor")
# plt.show()


# # ex 4 - scatter plot
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

# #citire din fiesier csv
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


# ex 5 - Cerinta:
# Folositi Spectra Forecast. Semnalul A va fi reprezentat de coloana "Vanzari" iar semnalul B va fi
# reprezentat de coloana "Target". Plotati semnalul M pentru d= 50

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


# #ex Buton care afiseaza graficul
# # Poate fi folosit pentru a ascunde graficul,
# # iar prin intermediul butonului, sa deschidem graficul in alta fereastra
# import tkinter as tk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
#
# def deseneaza_plot():
#     ax.clear()
#     ax.plot(x, y)
#     ax.set_xlabel("X")
#     ax.set_ylabel("Y")
#     ax.set_title("Line plot")
#     canvas.draw()
#
#
# x = [1, 2, 3, 4, 5]
# y = [10, 14, 13, 18, 20]
#
# root = tk.Tk()
# root.title("Plot in aceeasi fereastra")
# root.geometry("700x500")
#
# buton = tk.Button(root, text="Afiseaza plot", command=deseneaza_plot)
# buton.pack(pady=10)
#
# fig = Figure(figsize=(6, 4), dpi=100)
# ax = fig.add_subplot(111)
#
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#
# root.mainloop()

#ex
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def deseneaza_plot():
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

buton = tk. Button(root, text="Afiseaza plot", command=deseneaza_plot)
buton.pack(pady=10)

fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()
