import tkinter as tk
from tkinter import messagebox

def solve():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = float(entry_d.get())
        e = float(entry_e.get())
        f = float(entry_f.get())

        # a*x + b*y = c
        # d*x + e*y = f
        determinant = a * e - b * d
        dx = c * e - b * f
        dy = a * f - c * d

        if abs(determinant) > 1e-10:
            x = dx / determinant
            y = dy / determinant
            result_label.config(text=f"x = {x:.4g};  y = {y:.4g}")
        elif abs(dx) < 1e-10 and abs(dy) < 1e-10:
            result_label.config(text="Система має безліч розв'язків.")
        else:
            result_label.config(text="Система не має розв'язків.")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числа в усі поля.")

root = tk.Tk()
root.title("Розв'язання системи рівнянь")
root.geometry("420x320")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack()

tk.Label(
    frame,
    text="Система: a*x + b*y = c; d*x + e*y = f"
).grid(row=0, column=0, columnspan=6, pady=8)

entries = {}
for index, name in enumerate(("a", "b", "c", "d", "e", "f")):
    row = 1 + index // 3
    col = (index % 3) * 2
    tk.Label(frame, text=f"{name} =").grid(row=row, column=col, padx=4, pady=6)
    field = tk.Entry(frame, width=8)
    field.grid(row=row, column=col + 1, padx=4, pady=6)
    entries[name] = field

entry_a, entry_b, entry_c = entries["a"], entries["b"], entries["c"]
entry_d, entry_e, entry_f = entries["d"], entries["e"], entries["f"]

tk.Button(frame, text="Розв'язати", command=solve).grid(
    row=3, column=0, columnspan=6, pady=12
)

result_label = tk.Label(frame, text="Введіть коефіцієнти системи.")
result_label.grid(row=4, column=0, columnspan=6, pady=8)

root.mainloop()
