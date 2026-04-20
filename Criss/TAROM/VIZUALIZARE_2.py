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




