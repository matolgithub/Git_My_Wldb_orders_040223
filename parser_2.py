import os
from os import getenv
from requests import get
from bs4 import BeautifulSoup as bs
from fake_headers import Headers
from dotenv import load_dotenv
from tkinter import *
from tkinter import messagebox
from pprint import pprint

load_dotenv()

url = getenv("URL_2")
headers = Headers().generate()

id_catalog = ""
id_picture = ""

not_for_war = []
for_war = []


# def main_form():
#     window = Tk()
#     window.title("Подбор экипировки для братана")
#     text_1 = "Нажмите кнопку!"
#     # text_2 = "Игорь! Привет! Я Чэвэкашка! Олег попросил немного помочь тебе. Что будем делать?"
#     text_instruction_1 = Label(text=text_1, fg='white', bg='black')
#     text_instruction_1.grid(row=7, column=1, padx=5, pady=10, sticky="w")
#
#     background_image = PhotoImage(file="pictures/com.png")
#     background_label = Label(window, image=background_image)
#     background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
#     canvas = Canvas(width=430, height=380)
#     canvas.grid(row=1, column=1, padx=15, pady=15, sticky="nesw")
#     img = PhotoImage(file='pictures/111.png').subsample(2, 2)
#     canvas.create_image(0, 0, anchor=NW, image=img)
#
#     def exit_form():
#         window.destroy()
#         text_exit_1 = 'Работа приложения'
#         text_exit_2 = 'Благодарим, работа закончена!'
#         messagebox.showinfo(text_exit_1, text_exit_2)

def scrape_func():
    response_text = get(url=url, headers=headers).text
    response_json = get(url=url, headers=headers).json
    response_status = get(url=url, headers=headers).status_code
    # pprint(response_text)
    # pprint(response_json)
    pprint(response_status)
    soup = bs(response_text, "lxml")
    pprint(soup)

    return soup


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
    pprint(image_list)
    # pprint(data_pic_list_2)

    return link_list, image_list


if __name__ == "__main__":
    # scrape_func()
    read_data_1()
