import os
import csv

cale = os.path.join(os.path.dirname(os.path.abspath(__file__)), "angajati.csv")

with open(cale, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    randuri = list(reader)

angajati_it = []
salariu_total = 0
salariu_maxim = -1
cel_mai_bine_platit = None

for rand in randuri:
    salariu = int(rand["salariu"])
    salariu_total += salariu

    if rand["departament"] == "IT":
        angajati_it.append(rand)

    if salariu > salariu_maxim:
        salariu_maxim = salariu
        cel_mai_bine_platit = rand

print("Angajati IT:")
for ang in angajati_it:
    print(ang["nume"], ang["salariu"])

print("Salariu mediu:", salariu_total / len(randuri))
print("Salariu maxim:", cel_mai_bine_platit["nume"], salariu_maxim)
