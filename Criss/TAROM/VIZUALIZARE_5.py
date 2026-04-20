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
