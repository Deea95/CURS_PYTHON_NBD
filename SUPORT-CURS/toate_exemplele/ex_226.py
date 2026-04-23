import tkinter as tk


def draw_chart(canvas, q, c, e):
    s = [int(i) for i in q.split(',')]
    max_value = max(s)

    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    if e == 'y':
        canvas.delete("all")

    canvas.create_rectangle(0, 0, width, height, fill="#f1f1f1")

    prev_x = None
    prev_y = None

    step = width / (len(s) - 1)

    for i in range(len(s)):
        y = height - (height / max_value * s[i])
        x = step * i

        # text pe punct
        canvas.create_text(
            x, y,
            text=str(s[i]),
            font=("Arial", 12),
            fill="black",
            anchor='w'
        )

        if prev_x is not None and prev_y is not None:
            canvas.create_line(prev_x, prev_y, x, y, fill=c, width=2)

        prev_x, prev_y = x, y


def create_chart_window():
    root = tk.Tk()
    root.title("Chart")

    canvas = tk.Canvas(root, height=300, width=1100)
    canvas.pack()

    entry = tk.Entry(root)
    entry.insert(0, "23,45,66,77,44,33,99")
    entry.pack()

    def plot_chart():
        data = entry.get()
        draw_chart(canvas, data, '#ff0000', 'y')

    button = tk.Button(root, text="Plot chart!", command=plot_chart)
    button.pack()

    root.mainloop()


create_chart_window()