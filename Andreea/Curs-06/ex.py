import tkinter as tk
import requests
import threading

def fetch():
    url = 'https://ucp.crowland.ro'
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            text = response.text
        else:
            text = f"Eroare: {response.status_code}"

    except Exception as e:
        text = str(e)

    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, text)


def citeste():
    threading.Thread(target=fetch, daemon=True).start()


root = tk.Tk()
root.geometry("500x300")

btn = tk.Button(root, text="Citeste fisier", command=citeste)
btn.place(x=150, y=20, width=200, height=40)

textbox = tk.Text(root)
textbox.place(x=50, y=80, width=350, height=180)

scroll = tk.Scrollbar(root, command=textbox.yview)
scroll.place(x=400, y=80, height=180)

textbox.config(yscrollcommand=scroll.set)

root.mainloop()