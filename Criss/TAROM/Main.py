import pandas as pd
import matplotlib.pyplot as plt

# Date dummy despre zboruri TAROM
data = {
    "Destinatie": ["Paris", "Londra", "Roma", "Madrid", "Berlin"],
    "Pasageri": [120, 150, 100, 130, 90],
    "Pret Mediu (€)": [200, 250, 180, 220, 170],
    "Grad Ocupare (%)": [75, 85, 70, 80, 65]
}

df = pd.DataFrame(data)

print(df)

import matplotlib.pyplot as plt
import numpy as np


# Vizualizare 1 – Bar chart (pasageri per destinație)
#  1. Sortare descrescătoare
df = df.sort_values(by="Pasageri", ascending=False)

#  2. Gradient de culori
colors = plt.cm.Blues(np.linspace(0.4, 1, len(df)))

#  3. Plot
plt.figure()
bars = plt.bar(df["Destinatie"], df["Pasageri"], color=colors)

plt.title("Numar pasageri per destinatie (sortat descrescator)")
plt.xlabel("Destinatie")
plt.ylabel("Pasageri")

#  4. Adăugare valori pe fiecare bară
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height - 5,  # poziție în interiorul barei
        f'{int(height)}',
        ha='center',
        va='top',
        color='white',
        fontsize=10,
        fontweight='bold'
    )

plt.show()


# Vizualizare 2 – Line chart (prețuri)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(data)

plt.figure()

# Linie
plt.plot(df["Destinatie"], df["Pret Mediu (€)"], marker='o')

# Area (zona umplută)
plt.fill_between(df["Destinatie"], df["Pret Mediu (€)"], alpha=0.3)

plt.title("Pret mediu bilet TAROM (line + area)")
plt.xlabel("Destinatie")
plt.ylabel("Pret (€)")

# Valori pe fiecare punct
for i, value in enumerate(df["Pret Mediu (€)"]):
    plt.text(
        i,
        value + 2,   # puțin deasupra punctului
        str(value),
        ha='center'
    )

plt.show()



# Vizualizare 3 – Pie chart (grad de ocupare)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(data)

#  format valori + procente
def autopct_format(values):    # Valori + procente: autopct=autopct_format(...)
    def inner(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f"{pct:.1f}%\n({val})"
    return inner

plt.figure()

wedges, texts, autotexts = plt.pie(
    df["Grad Ocupare (%)"],
    labels=df["Destinatie"],
    autopct=autopct_format(df["Grad Ocupare (%)"]),
    startangle=90,
    shadow=True,   # Umbră
    pctdistance=0.75,  # 🔥 cheia: poziționează textul în mijlocul feliei
    wedgeprops=dict(width=0.4, edgecolor='black')   # Formă de gogoasă: wedgeprops=dict(width=0.4)
                                                   # Contur: edgecolor='black'

)
plt.title("Grad de ocupare zboruri TAROM (Donut Chart)")

plt.show()



# Vizualizare 4 – Scatter plot (preț vs pasageri)
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# culori bazate pe pret (Gradient pe culori)
colors = df["Pret Mediu (€)"]

# dimensiune puncte (Bubble chart)
sizes = df["Pasageri"] * 5

scatter = plt.scatter(
    df["Pret Mediu (€)"],
    df["Pasageri"],
    c=colors,
    s=sizes,
    alpha=0.7
)

# colorbar (legendă culori)
plt.colorbar(scatter, label="Pret (€)")

# etichete moderne
for i in range(len(df)):
    plt.text(
        df["Pret Mediu (€)"][i],
        df["Pasageri"][i],
        df["Destinatie"][i],
        fontsize=9,
        ha='center',
        va='center'
    )

# styling modern
plt.title("Analiza TAROM: Pret vs Pasageri", fontsize=14)
plt.xlabel("Pret mediu (€)")
plt.ylabel("Numar pasageri")

plt.grid(alpha=0.3)

plt.show()
