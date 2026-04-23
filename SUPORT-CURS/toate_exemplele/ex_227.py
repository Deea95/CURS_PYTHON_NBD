# import requests
#
#
# # -------------------------
# # VERSION 1: simple GET
# # -------------------------
# url = 'https://www.springer.com'
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     html_content = response.text
#     print(html_content)
# else:
#     print("Failed to retrieve the webpage")
#
#
# # -------------------------
# # VERSION 2: GET with params
# # -------------------------
# url = 'https://springer.com/api'
#
# params = {
#     'param1': 'value1',
#     'param2': 'value2'
# }
#
# response = requests.get(url, params=params)
#
# if response.status_code == 200:
#     print(response.text)
# else:
#     print("Failed to retrieve data. Status code:", response.status_code)
#
#
from http.client import responses


# ex
import requests
import tkinter as tk

def citeste():
    url = 'https://www.springer.com'

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        print(html_content)
    else:
        print("Failed to retrieve the webpage")
    text=response.text
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, text)

root = tk.Tk()
root.geometry("500x300")

btn = tk.Button(root, text="Citeste fisier", command=citeste)
btn.place(x=150, y=20, width=200, height=40)

# Textbox
textbox = tk.Text(root)
textbox.place(x=50, y=80, width=350, height=180)

# Scrollbar vertical
scroll = tk.Scrollbar(root, command=textbox.yview)
scroll.place(x=400, y=80, height=180)

# Legătură Text « Scroll
textbox.config(yscrollcommand=scroll.set)

root.mainloop()



# continutul dintr o var text l-am scris in var textbox, apoi urmatoarea etapa este: din texbox il vom scrie in fisier