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


