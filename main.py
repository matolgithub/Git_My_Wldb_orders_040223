import os
from os import getenv
from requests import get
from bs4 import BeautifulSoup as bs
from fake_headers import Headers
from dotenv import load_dotenv
from tkinter import *
from tkinter import messagebox
import time
import webbrowser
from urllib.request import urlopen
from PIL import ImageTk, Image
from io import BytesIO

load_dotenv()

# url = getenv("URL")
url = getenv("URL_2")
headers = Headers().generate()

id_catalog = ""
id_picture = ""

not_for_war = [4, 7, 23, 58, 68, 69]
for_war = [96, 99, 100, 101, 102, 103]


# def speaker_text(text):
#     tts = pyttsx3.init()
#     voices = tts.getProperty('voices')
#     tts.setProperty('voice', 'ru')
#     tts.say(f'{text}')
#     tts.runAndWait()
#     return text


def main_form():
    window = Tk()
    window.title("Подбор экипировки для братана")
    text_1 = "Нажмите кнопку!"
    # text_2 = "Игорь! Привет! Я Чэвэкашка! Олег попросил немного помочь тебе. Что будем делать?"
    text_instruction_1 = Label(text=text_1, fg='white', bg='black')
    text_instruction_1.grid(row=7, column=1, padx=5, pady=10, sticky="w")

    background_image = PhotoImage(file="pictures/com.png")
    background_label = Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas = Canvas(width=430, height=380)
    canvas.grid(row=1, column=1, padx=15, pady=15, sticky="nesw")
    img = PhotoImage(file='pictures/111.png').subsample(2, 2)
    canvas.create_image(0, 0, anchor=NW, image=img)

    def exit_form():
        window.destroy()
        text_exit_1 = 'Работа приложения'
        text_exit_2 = 'Благодарим, работа закончена!'
        messagebox.showinfo(text_exit_1, text_exit_2)

    def scrape_func():
        response_text = get(url=url, headers=headers).text
        response_json = get(url=url, headers=headers).json
        response_status = get(url=url, headers=headers).status_code
        # pprint(response_text)
        # pprint(response_json)
        # pprint(response_status)
        soup = bs(response_text, "lxml")
        # pprint(soup)

        return soup

    def read_data_1(data_file="data.txt"):
        total_data_list = []
        unit_number = 1
        with open(data_file, "r") as file:
            content = file.read()
            soup = bs(content, "lxml")
            data_price_list = soup.findAll("p", "archive-item__price")
            data_goods_list = soup.findAll("p", "archive-item__brand")
            data_img_link_list = soup.findAll("img")
            data_id_picture = soup.findAll("li", "archive-page__item archive-item")
        # print(len(data_goods_list), len(data_price_list), len(data_img_link_list), len(data_id_picture))
        # pprint(data_id_picture)
        for good_number in range(len(data_goods_list)):
            sku = str(data_goods_list[good_number])[31:-4]
            price_str = str(data_price_list[good_number]).replace("\xa0", "").replace(" ", "")[63:-37]
            price_int = int(str(data_price_list[good_number]).replace("\xa0", "").replace(" ", "")[63:-38])
            link_basket = "https:" + str(data_img_link_list[good_number]).replace(" ", "").replace('"', "")[18:-11]
            id_catalog = link_basket.split("/")[5]
            id_picture = str(data_id_picture[good_number]).replace(" ", "")[55:64].replace('"', '')
            url_picture = f"https://www.wildberries.ru/catalog/{id_catalog}/detail.aspx?size={id_picture}"
            link_pic = url_picture
            total_data_list.append(
                {unit_number: [sku, price_str, price_int, link_basket, url_picture]})
            unit_number += 1
        # pprint(total_data_list)

        return total_data_list

    def read_data_2(data_file="data_2.txt"):
        link_list = []
        image_list = []
        unit_number = 1
        with open(data_file, "r") as file:
            content = file.read()
            soup = bs(content, "lxml")
            data_link_list_2 = soup.findAll("a", "goods-card__container j-product-popup")
            data_pic_list_2 = soup.findAll("img")

        for good_number in range(len(data_link_list_2)):
            link = "https://www.wildberries.ru/" + str(data_link_list_2[good_number]).replace(" ", "").replace('"', "")[
                                                   50:94].replace(">", "").replace("<", "")
            link_list.append(link)
            unit_number += 1
        unit_number = 1
        for good_number in data_pic_list_2:
            image = "https:" + str(good_number).split('src="')[1][:70].split('"')[0]
            image_list.append(image)
            unit_number += 1
        # pprint(link_list)
        # pprint(image_list)
        # pprint(data_pic_list_2)

        return link_list, image_list

    def get_list():
        root = Toplevel(window)
        root.title("Работа с файлами")
        w, h, x, y = 1360, 850, 500, 100
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        root.grid_rowconfigure(index=0, weight=1)
        root.grid_columnconfigure(index=0, weight=1)
        root.grid_columnconfigure(index=1, weight=1)

        text_open = Text(root, width=300, height=500, bg="black", fg="white", wrap=WORD)
        text_open.grid(column=0, columnspan=1, row=0)

        with open("result.txt", "r") as file:
            text = file.read()
            text_open.delete("1.0", END)
            text_open.insert("1.0", text)

        root.mainloop()

    def write_data(file_name="data_result.txt"):
        list_data = read_data_1()
        num = 1
        file_path = os.getcwd()

        with open(file_name, "w", encoding="utf-8") as new_file:
            for item in list_data:
                for key, value in item.items():
                    result_string = f"{num}:! {value[0]}! {value[1]}! {value[3]}! {value[4]}\n{value[2]}"
                    if key not in not_for_war and key <= 70 or key in for_war:
                        new_file.write(f"{result_string}\n")
                        num += 1

        text_write_1 = 'Работа приложения'
        text_write_2 = f'Данные по снаряжению записаны в файл: {file_name}, который расположен в каталоге: {file_path}.'
        messagebox.showinfo(text_write_1, text_write_2)

    def write_result_txt(file_name="result.txt"):
        list_data = read_data_1()
        num = 1
        file_path = os.getcwd()

        with open(file_name, "w", encoding="utf-8") as new_file:
            for item in list_data:
                for key, value in item.items():
                    result_string = f"{num}:  {value[0]}      Цена - {value[1]}\n----------------------------------"
                    if key not in not_for_war and key <= 70 or key in for_war:
                        new_file.write(f"{result_string}\n")
                        num += 1

        text_write_txt_1 = 'Работа приложения'
        text_write_txt_2 = f'Данные по снаряжению записаны в файл: {file_name}, который расположен в каталоге: {file_path}.'
        messagebox.showinfo(text_write_txt_1, text_write_txt_2)

    def get_links():
        list_data = read_data_1()
        list_wild = []
        list_pic = []
        list_names = []
        for item in list_data:
            for key, value in item.items():
                if key not in not_for_war and key <= 70 or key in for_war:
                    list_wild.append(value[4])
                    list_pic.append(value[3])
                    list_names.append(value[0])

        return list_pic, list_wild, list_names

    def new_window():
        list_pic, list_wild, list_names = get_links()
        root = Toplevel(window)
        root.configure(borderwidth=2)
        root.title("Военная экипировка и снаряга!")
        w, h, x, y = 1360, 850, 500, 100
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        text_wait_1 = 'Работа приложения'
        text_wait_2 = 'Закройте это сообщение и подождите. Готовится форма.'
        messagebox.showinfo(text_wait_1, text_wait_2, parent=root)

        background_image = PhotoImage(file="pictures/com_2.png")
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def push_button(item):
            text_push_1 = 'Форма диалога.'
            text_push_2 = "Вывести картинку этого товара?"

            text_push_3 = 'Форма диалога.'
            text_push_4 = "Хотите посмотреть этот товар в 'Wildberries'?"

            text_push_5 = 'Форма диалога.'
            text_push_6 = "Форму закрыть и перейти в главное меню?"

            ask_form_1 = messagebox.askquestion(text_push_1, text_push_2, parent=root)
            if ask_form_1 == 'no':
                ask_form_2 = messagebox.askquestion(text_push_3, text_push_4, parent=root)
                if ask_form_2 == 'no':
                    ask_form_3 = messagebox.askquestion(text_push_5, text_push_6, parent=root)
                    if ask_form_3 == "no":
                        text_contin_1 = 'Работа приложения'
                        text_contin_2 = 'Тогда продолжаем.'
                        messagebox.showinfo(text_contin_1, text_contin_2, parent=root)
                    else:
                        text_exit_1 = 'Работа приложения'
                        text_exit_2 = 'Тогда работа с этой формой закончена!'
                        messagebox.showinfo(text_exit_1, text_exit_2, parent=root)
                        root.destroy()
                else:
                    webbrowser.open(list_wild[item])
            else:
                webbrowser.open(list_pic[item])
                time.sleep(5)
                ask_form_2 = messagebox.askquestion(text_push_3, text_push_4, parent=root)
                if ask_form_2 == 'no':
                    ask_form_3 = messagebox.askquestion(text_push_5, text_push_6, parent=root)
                    if ask_form_3 == "no":
                        text_contin_1 = 'Работа приложения'
                        text_contin_2 = 'Тогда продолжаем.'
                        messagebox.showinfo(text_contin_1, text_contin_2, parent=root)
                    else:
                        text_exit_1 = 'Работа приложения'
                        text_exit_2 = 'Тогда работа с этой формой закончена!'
                        messagebox.showinfo(text_exit_1, text_exit_2, parent=root)
                        root.destroy()
                else:
                    webbrowser.open(list_wild[item])

        def exit_new_form():
            root.destroy()
            text_exit_1 = 'Работа приложения'
            text_exit_2 = 'Форма с кнопками, фото и ссылками закрыта!'
            messagebox.showinfo(text_exit_1, text_exit_2)

        def set_button(i):
            # print(i, list_pic[i])

            with urlopen(list_pic[i]) as u:
                raw_data = u.read()
            img = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(img.resize((7, 9), Image.LANCZOS))
            num = i
            Button(root, text=list_names[i], command=lambda item=num: push_button(item=item), width=7, height=8,
                   wraplength=70).grid(row=y, column=x, padx=2, pady=2)

        y = 0
        x = 0
        for i in range(70):
            set_button(i)
            x += 1
            if x > 14:
                x = 0
                y += 1

        Button(root, text="ВЫХОД", command=exit_new_form, bg="red", fg="white").grid(row=5, column=14, padx=2,
                                                                                     pady=2)

        root.mainloop()

    def new_window_2():
        list_pic, list_wild, list_names = get_links()
        root = Toplevel(window)
        root.configure(borderwidth=2)
        root.title("Военная экипировка и снаряга!")
        w, h, x, y = 1360, 700, 500, 100
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        text_wait_1 = 'Работа приложения'
        text_wait_2 = 'Закройте это сообщение и подождите. Готовится форма.'
        messagebox.showinfo(text_wait_1, text_wait_2, parent=root)

        background_image = PhotoImage(file="pictures/com_2.png")
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def push_button(item):
            text_push_1 = 'Форма диалога.'
            text_push_2 = "Вывести крупную картинку этого товара?"

            text_push_3 = 'Форма диалога.'
            text_push_4 = "Хотите посмотреть этот товар в 'Wildberries'?"

            text_push_5 = 'Форма диалога.'
            text_push_6 = "Форму закрыть и перейти в главное меню?"

            ask_form_1 = messagebox.askquestion(text_push_1, text_push_2, parent=root)
            if ask_form_1 == 'no':
                ask_form_2 = messagebox.askquestion(text_push_3, text_push_4, parent=root)
                if ask_form_2 == 'no':
                    ask_form_3 = messagebox.askquestion(text_push_5, text_push_6, parent=root)
                    if ask_form_3 == "no":
                        text_contin_1 = 'Работа приложения'
                        text_contin_2 = 'Тогда продолжаем.'
                        messagebox.showinfo(text_contin_1, text_contin_2, parent=root)
                    else:
                        text_exit_1 = 'Работа приложения'
                        text_exit_2 = 'Тогда работа с этой формой закончена!'
                        messagebox.showinfo(text_exit_1, text_exit_2, parent=root)
                        root.destroy()
                else:
                    webbrowser.open(list_wild[item])
            else:
                webbrowser.open(list_pic[item])
                time.sleep(5)
                ask_form_2 = messagebox.askquestion(text_push_3, text_push_4, parent=root)
                if ask_form_2 == 'no':
                    ask_form_3 = messagebox.askquestion(text_push_5, text_push_6, parent=root)
                    if ask_form_3 == "no":
                        text_contin_1 = 'Работа приложения'
                        text_contin_2 = 'Тогда продолжаем.'
                        messagebox.showinfo(text_contin_1, text_contin_2, parent=root)
                    else:
                        text_exit_1 = 'Работа приложения'
                        text_exit_2 = 'Тогда работа с этой формой закончена!'
                        messagebox.showinfo(text_exit_1, text_exit_2, parent=root)
                        root.destroy()
                else:
                    webbrowser.open(list_wild[item])

        def exit_new_form():
            root.destroy()
            text_exit_1 = 'Работа приложения'
            text_exit_2 = 'Форма с кнопками, фото и ссылками закрыта!'
            messagebox.showinfo(text_exit_1, text_exit_2)

        list_photos = []
        for i in list_pic:
            with urlopen(i) as u:
                raw_data = u.read()
            img = Image.open(BytesIO(raw_data))
            list_photos.append(ImageTk.PhotoImage(img.resize((80, 100), Image.LANCZOS)))
        y = 0
        x = 0
        num = 0
        for photo in list_photos:
            Button(root, image=photo, command=lambda item=num: push_button(item=item), width=80, height=100).grid(row=y,
                                                                                                                  column=x,
                                                                                                                  padx=2,
                                                                                                                  pady=10)
            num += 1
            x += 1
            if x > 14:
                x = 0
                y += 1

        Button(root, text="ВЫХОД", command=exit_new_form, bg="red", fg="white").grid(row=5, column=14, padx=2,
                                                                                     pady=2)

        root.mainloop()

    def new_window_3():
        list_pic, basket_list = read_data_2()
        root = Toplevel(window)
        root.configure(borderwidth=2)
        root.title("Дополнительная экипировка и снаряга!")
        w, h, x, y = 560, 800, 650, 100
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        text_wait_1 = 'Работа приложения'
        text_wait_2 = 'Закройте это сообщение и подождите. Готовится форма.'
        messagebox.showinfo(text_wait_1, text_wait_2, parent=root)

        background_image = PhotoImage(file="pictures/com_2.png")
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def push_button(item):
            text_push_3 = 'Форма диалога.'
            text_push_4 = "Хотите посмотреть этот товар в 'Wildberries'?"

            text_push_5 = 'Форма диалога.'
            text_push_6 = "Форму закрыть и перейти в главное меню?"

            ask_form_2 = messagebox.askquestion(text_push_3, text_push_4, parent=root)
            if ask_form_2 == 'no':
                ask_form_3 = messagebox.askquestion(text_push_5, text_push_6, parent=root)
                if ask_form_3 == "no":
                    text_contin_1 = 'Работа приложения'
                    text_contin_2 = 'Тогда продолжаем.'
                    messagebox.showinfo(text_contin_1, text_contin_2, parent=root)
                else:
                    text_exit_1 = 'Работа приложения'
                    text_exit_2 = 'Тогда работа с этой формой закончена!'
                    messagebox.showinfo(text_exit_1, text_exit_2, parent=root)
                    root.destroy()
            else:
                webbrowser.open(list_pic[item])

        def exit_new_form():
            root.destroy()
            text_exit_1 = 'Работа приложения'
            text_exit_2 = 'Форма с кнопками, фото и ссылками закрыта!'
            messagebox.showinfo(text_exit_1, text_exit_2)

        list_photos = []
        for i in basket_list:
            with urlopen(i) as u:
                raw_data = u.read()
            img = Image.open(BytesIO(raw_data))
            list_photos.append(ImageTk.PhotoImage(img.resize((100, 120), Image.LANCZOS)))
        y = 0
        x = 0
        num = 0
        for photo in list_photos:
            Button(root, image=photo, command=lambda item=num: push_button(item=item), width=100, height=120).grid(
                row=y,
                column=x,
                padx=2,
                pady=10)
            num += 1
            x += 1
            if x > 4:
                x = 0
                y += 1

        Button(root, text="ВЫХОД", command=exit_new_form, bg="red", fg="white").grid(row=5, column=4, padx=2,
                                                                                     pady=2)

        root.mainloop()

    button_1 = Button(text="Получить список военного снаряжения", activebackground='red', highlightcolor='red',
                      bg='black', fg='white', command=get_list)
    button_2 = Button(text="Записать список в файл", activebackground='red',
                      highlightcolor='red', bg='black', fg='white', command=write_result_txt)
    button_3 = Button(text="Открыть форму с названиями товара", activebackground='red',
                      highlightcolor='red', bg='black', fg='white', command=new_window)
    button_4 = Button(text="Открыть форму с фото", activebackground='red',
                      highlightcolor='red', bg='black', fg='white', command=new_window_2)
    button_5 = Button(text="Интересные элементы экипировки", activebackground='red',
                      highlightcolor='red', bg='black', fg='white', command=new_window_3)
    button_6 = Button(text="ВЫХОД", activebackground='red', highlightcolor='red', bg='black', fg='white',
                      command=exit_form)
    button_1.grid(row=3, column=1, padx=30, pady=20, sticky='nesw')
    button_2.grid(row=4, column=1, padx=30, pady=20, sticky='nesw')
    button_3.grid(row=5, column=1, padx=30, pady=20, sticky='nesw')
    button_4.grid(row=6, column=1, padx=30, pady=20, sticky='nesw')
    button_5.grid(row=7, column=1, padx=30, pady=20, sticky='nesw')
    button_6.grid(row=8, column=1, padx=30, pady=20, sticky='nesw')

    # speaker_text(text_2 + text_1)

    window.mainloop()


if __name__ == "__main__":
    main_form()
