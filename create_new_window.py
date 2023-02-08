import tkinter as tk


def create_window():
    window = tk.Toplevel(root)
    # Добавление элементов в window
    ...


root = tk.Tk()
b = tk.Button(root, text="Create new window", command=create_window)
b.pack()
root.mainloop()
