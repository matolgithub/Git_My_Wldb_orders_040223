import time
from tkinter import *
from tkinter.ttk import *
import webbrowser
from tkinter import messagebox

root = Tk()
root.configure(bg="black", borderwidth=2)
root.title("Военная экипировка и снаряга!")
root.geometry("1900x850")

url = "https://www.wildberries.ru/catalog/137790056/detail.aspx?size=234503434"
url_pic = "https://basket-10.wb.ru/vol1377/part137790/137790056/images/c516x688/1.jpg"

background_image = PhotoImage(file="pictures/com.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def push_button():
    text_push_1 = 'Форма диалога.'
    text_push_2 = "Вывести картинку покрупнее?"

    text_push_3 = 'Форма диалога.'
    text_push_4 = "Хотите посмотреть этот товар в 'Wildberries'?"

    ask_form_1 = messagebox.askquestion(text_push_1, text_push_2)
    if ask_form_1 == 'no':
        ask_form_2 = messagebox.askquestion(text_push_3, text_push_4)
        if ask_form_2 == 'no':
            text_exit_1 = 'Работа приложения'
            text_exit_2 = 'Тогда работа закончена!'
            messagebox.showinfo(text_exit_1, text_exit_2)
            root.quit()
        else:
            webbrowser.open(url)
    else:
        webbrowser.open(url_pic)
        time.sleep(5)
        ask_form_2 = messagebox.askquestion(text_push_3, text_push_4)
        if ask_form_2 == 'no':
            text_exit_1 = 'Работа приложения'
            text_exit_2 = 'Тогда работа закончена!'
            messagebox.showinfo(text_exit_1, text_exit_2)
            root.quit()
        else:
            webbrowser.open(url)


def exit_form():
    root.quit()
    text_exit_1 = 'Работа приложения'
    text_exit_2 = 'Спасибо, работа закончена!'
    messagebox.showinfo(text_exit_1, text_exit_2)


photo = PhotoImage(file="pictures/1.png")
photoimage = photo.subsample(8, 8)

photo_quit = PhotoImage(file="pictures/quit.png")
photoimage_quit = photo_quit.subsample(4, 4)

y = 0
x = 0
for i in range(71):
    Button(root, image=photoimage, command=push_button, width=30).grid(row=y, column=x, padx=2, pady=2)
    x += 1
    if x > 14:
        x = 0
        y += 1

Button(root, image=photoimage_quit, command=exit_form, width=30).grid(row=5, column=14, padx=2, pady=2)

root.mainloop()
