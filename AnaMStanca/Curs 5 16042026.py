# EXCEL,CITITRE,SCRIERE,MANIPULARE
'''
import pandas as pd

# creare tabel
df = pd.DataFrame({
    "nume": ["Ana", "Ion"],
    "nota": [9, 7]
})

# salvare exel

df.to_excel("note.xlsx", index=False)

# citire excel
df2 = pd.read_excel("note.xlsx")

# manipulare
df2["nota"] = df2["nota"] + 1
print(df2)

'''
'''
import random

with open("date_mari.txt","w") as f:
    for i in range(100000):
        numar = random.randint(1,1000)
        f.write(str(numar)+"\n")
'''
'''
total=0
count=0

with open("date_mari.txt","r") as f:
    for line in f:
        total+=int(line)
        count+=1
print(total/count)
'''
'''
import tkinter as tk
import random

def afiseaza():
    text=entry.get()
    label.config(text="Ai scris:"+text)
    with open("teste.txt", "w") as f:
        for i in range(int(text)):
            numar = random.randint(1,1000)
            f.write(str(numar) + "\n")

root = tk.Tk()
root.title("Exemplu GUI")

entry = tk.Entry(root)
entry.pack()

buton = tk.Button(root, text="Apasa", command=afiseaza)
buton.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
'''

'''
import tkinter as tk

def afiseaza():
    text=entry.get()
    label.config(text="Ai scris:"+text)

root = tk.Tk()
root.title("Exemplu GUI")
root.geometry("400x250") #dimensiune fereastra


#Buton
buton = tk.Button(root, text="Apasa", command=afiseaza)
buton.place(x=100,y=40,width=200,height=30)

#Input
entry = tk.Entry(root)
entry.place(x=150,y=90,width=100,height=40)


#label rezultat
label = tk.Label(root, text="")
label.place(x=100,y=150,width=200,height=30)

root.mainloop()
'''

'''
import tkinter as tk

def calc():
    a=int(e1.get())
    b=int(e2.get())
    rez.config(text=str(a+b))

root = tk.Tk()
root.geometry("300x200") #dimensiune fereastra


#Input
e1 = tk.Entry(root)
e1.place(x=50,y=30,width=80)

e2 = tk.Entry(root)
e2.place(x=170,y=30,width=80)

#Buton
btn = tk.Button(root, text="+", command=calc)
btn.place(x=120,y=70,width=60,height=30)

#label rezultat
rez = tk.Label(root, text="")
rez.place(x=100,y=120,width=100,height=30)

root.mainloop()
'''
'''
import tkinter as tk

def rosu():
   root.config(bg="rosu")

def verde():
       root.config(bg="verde")

root = tk.Tk()
root.geometry("300x200") #dimensiune fereastra


#Buton
b1 = tk.Button(root, text="Rosu", command=rosu)
b1.place(x=50,y=80,width=80,height=40)

b2 = tk.Button(root, text="Verde", command=verde)
b2.place(x=170,y=80,width=80,height=40)



root.mainloop()

'''
'''
import tkinter as tk

def rosu():
    root.config(bg="red")

def verde():
    root.config(bg="green")

def verifica():
    if entry.get()=="1234":
        label.config(text="Corect")
        rosu()
    else:
        verde()
        label.config(text="Gresit")

root = tk.Tk()
root.geometry("300x200")

entry=tk.Entry(root,show="*" )
entry.place(x=80,y=40,width=140)

btn=tk.Button(root,text="Check",command=verifica)
btn.place(x=100,y=80,width=100,height=30)

label=tk.Label(root,text="")
label.place(x=100,y=130,width=100)

root.mainloop()
'''


'''
import tkinter as tk
def citeste():
    #with open(r"C:\Users\Ana-MariaStanca\PycharmProjects\PythonProject\teste.txt","r") as f:
        text=f.read()
    label.config(text=text[:50])

root = tk.Tk()
root.geometry("400x200")

btn=tk.Button(root,text="Citeste fisier",command=citeste)
btn.place(x=50,y=100,width=300,height=40)

root.mainloop()
'''

'''
import tkinter as tk

def citeste():
    with open(r"C:\Users\Ana-MariaStanca\PycharmProjects\PythonProject\teste.txt","r") as f:
        text=f.read()
    textbox.delete("1.0",tk.END)
    textbox.insert(tk.END,text)

root = tk.Tk()
root.geometry("400x200")

btn=tk.Button(root,text="Citeste fisier",command=citeste)
btn.place(x=50,y=100,width=300,height=40)

textbok=tk.Label(root)
textbok.place(x=50,y=80,width=350,height=40)

scroll = tk.Scrollbar(root,command=textbook.yview)
scroll.place(x=400,y=80,height=180)

textbok.config(yscrollcommand=scroll.set)

root.mainloop()
'''

def smooth(a):
    n=len(a)
    for i in range(1,n-1):
        a[i]=a[i-1]+a[i+1]/2
    return a

a=[5,1,8,4,6,2,9,8]

print(smooth(a))