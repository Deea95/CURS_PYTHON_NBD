'''
import json

txt = '{"v1":["a","b","c"],"v2":' + \
    '[[0,1,0],[1,1,1],[0,1,0]]' + \
    ',"v3":{"c1":["a","b","c"]' + \
    ',"c2":[[0,1,0],[1,1,1],[0' + \
    ',1,0]],"c3":42}}'
obj = json.loads(txt)
a = []
for i in obj['v3']['c1']:
    a.append(i)
print(a)

'''
'''
import json

txt = '{"v1":["a","b","c"],"v2":' + \
      '[[0,1,0],[1,1,1],[0,1,0]]' + \
      ',"v3":{"c1":["a","b","c"]' + \
      ',"c2":[[0,1,0],[1,1,1],[0' + \
      ',1,0]],"c3":42}}'

obj = json.loads(txt)
a = []

for i in range(len(obj['v3']['c2'])):
    a.append([])
    for j in range(len(obj['v3']['c2'][i])):
        a[i].append(obj['v3']['c2'][i][j])

def smc(m):
    r = ''
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + " "
        r += "\n"
    return r

print(smc(a))
'''
'''

import os
import csv

cale = os.path.join(os.path.dirname(os.path.abspath(__file__)),"angajati.csv")
with open(cale,"r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    randuri=list(reader)
    
angajati_it=[]
salariu_total=0
salariu_maxim=-1
cel_mai_bine_platit=None

for rand in randuri:
    salariu=int(rand["salariu"])
    salariu_total +=salariu

    if rand ["departament"]=="IT":
        angajati_it.append(rand)
        
    if salariu > salariu_maxim:
        salariu_maxim=salariu
        cel_mai_bine_platit=rand
        
print("Angati IT:")
for ang in angajati_it:
    print(ang["nume"],ang["salariu"])

print("Salariu mediu:",salariu_total/len(randuri))
print("")

'''


