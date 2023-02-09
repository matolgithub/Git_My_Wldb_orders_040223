from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Работа с файлами")
root.geometry("1500x900")

root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)

text_editor = Text(width=1300, height=700, bg="black", fg="white", wrap=WORD)
text_editor.grid(column=0, columnspan=2, row=0)

with open("data_result.txt", "r") as file:
    text = file.read()
    text_editor.delete("1.0", END)
    text_editor.insert("1.0", text)


# открываем файл в текстовое поле
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)


# сохраняем текст из текстового поля в файл
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)


open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)

save_button = ttk.Button(text="Сохранить файл", command=save_file)
save_button.grid(column=1, row=1, sticky=NSEW, padx=10)

root.mainloop()

# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
#
# interface = Tk()
#
#
# def openfile():
#     return filedialog.askopenfilename()
#
#
# button = ttk.Button(interface, text="Open", command=openfile)  # <------
# button.grid(column=1, row=1)
#
# interface.mainloop()
