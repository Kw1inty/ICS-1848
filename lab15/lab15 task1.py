import tkinter as tk

root = tk.Tk()
root.title("Кольори веселки")
root.geometry("320x260")
root.configure(bg="green")

colors = [
    ("Червоний", "red"),
    ("Помаранчевий", "orange"),
    ("Жовтий", "yellow"),
    ("Зелений", "green"),
    ("Блакитний", "skyblue"),
    ("Синій", "blue"),
    ("Фіолетовий", "violet"),
]

def change_color(name, color):
    root.configure(bg=color)
    with open("report.txt", "a", encoding="utf-8") as file:
        file.write(name + "\\n")

for name, color in colors:
    tk.Button(
        root,
        text=name,
        command=lambda n=name, c=color: change_color(n, c)
    ).pack()

root.mainloop()
