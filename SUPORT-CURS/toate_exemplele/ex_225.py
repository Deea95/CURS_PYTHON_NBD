import tkinter as tk
import matplotlib.pyplot as plt


# -------------------------
# TKINTER VERSION
# -------------------------
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

    for i in range(len(s)):
        y = height - (height / max_value * s[i])
        x = (width / len(s)) * i

        if prev_x is not None and prev_y is not None:
            canvas.create_line(prev_x, prev_y, x, y, fill=c, width=2)

        prev_x, prev_y = x, y


def create_chart_window(q, c, e):
    root = tk.Tk()
    root.title("Chart")

    canvas = tk.Canvas(root, height=300, width=1100)
    canvas.pack()

    draw_chart(canvas, q, c, e)

    root.mainloop()


# -------------------------
# MATPLOTLIB VERSION
# -------------------------
def chart(q, c, e):
    s = [int(val) for val in q.split(",")]
    mx = max(s)

    plt.figure(figsize=(11, 3))

    if e == 'y':
        plt.clf()

    plt.gca().set_facecolor("#f1f1f1")

    x = range(len(s))
    y = [mx - val for val in s]

    plt.plot(x, y, color=c, linewidth=2)

    plt.ylim(0, mx)

    plt.show()


# -------------------------
# RUN EXAMPLES
# -------------------------

# Tkinter chart
create_chart_window('23,45,66,77,44,33,99', '#ff0000', 'y')

# Matplotlib chart
chart('23,45,66,77,44,33,99', '#ff0000', 'y')