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