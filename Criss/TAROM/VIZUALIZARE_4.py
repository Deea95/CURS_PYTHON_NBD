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

# Vizualizare 4 – Scatter plot (preț vs pasageri)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # Date dummy
# data = {
#     "Destinatie": ["Paris", "Londra", "Roma", "Madrid", "Berlin"],
#     "Pasageri": [120, 150, 100, 130, 90],
#     "Pret Mediu (€)": [200, 250, 180, 220, 170],
#     "Grad Ocupare (%)": [75, 85, 70, 80, 65]
# }
#
# df = pd.DataFrame(data)
#
# plt.figure()

# 🎨 culori bazate pe pret
colors = df["Pret Mediu (€)"]

# 🔵 dimensiune puncte (bubble)
sizes = df["Pasageri"] * 5

scatter = plt.scatter(
    df["Pret Mediu (€)"],
    df["Pasageri"],
    c=colors,
    s=sizes,
    alpha=0.7
)

# 🌈 colorbar (legendă culori)
plt.colorbar(scatter, label="Pret (€)")

# 🏷 etichete moderne
for i in range(len(df)):
    plt.text(
        df["Pret Mediu (€)"][i],
        df["Pasageri"][i],
        df["Destinatie"][i],
        fontsize=9,
        ha='center',
        va='center'
    )

# ✨ styling modern
plt.title("Analiza TAROM: Pret vs Pasageri", fontsize=14)
plt.xlabel("Pret mediu (€)")
plt.ylabel("Numar pasageri")

plt.grid(alpha=0.3)

plt.show()