from os import getenv
from requests import get
from bs4 import BeautifulSoup as bs
from fake_headers import Headers
from pprint import pprint
from dotenv import load_dotenv
import lxml
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import pyttsx3

load_dotenv()

url = getenv("URL")
headers = Headers().generate()

id_catalog = ""
id_picture = ""

not_for_war = [4, 7, 23, 58, 68, 69]
for_war = [96, 99, 100, 101, 102, 103]


def speaker_text(text):
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', 'ru')
    tts.say(f'{text}')
    tts.runAndWait()
    return text


def main_form():
    window = Tk()
    window["bg"] = "black"
    window.title("Python - user form.")
    text_1 = "Нажмите кнопку!"
    text_2 = "Игорь! Привет! Я Чэвэкашка! Олег попросил немного помочь тебе. Что будем делать?"
    input_label_ID = Label(text=text_1, fg='white', bg='black')
    input_label_ID.grid(row=1, column=1, padx=5, pady=10, sticky="w")

    def exit_form():
        window.quit()

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

    def read_data():
        total_data_list = []
        unit_number = 1
        with open("data.txt", "r") as file:
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
        pprint(total_data_list)

        return total_data_list

    def write_data():
        list_data = read_data()
        num = 1

        with open("data_result.json", "w", encoding="utf-8") as new_file:
            for item in list_data:
                for key, value in item.items():
                    result_string = f"{num}:! {value[0]}! {value[1]}! {value[3]}! {value[4]}\n{value[2]}"
                    if key not in not_for_war and key <= 70 or key in for_war:
                        new_file.write(f"{result_string}\n")
                        num += 1

    button_1 = Button(text="Получить список военного снаряжения", activebackground='red', highlightcolor='red',
                      bg='blue', fg='white', command=read_data)
    button_2 = Button(text="Записать список в файл", activebackground='red',
                      highlightcolor='red', bg='blue', fg='white', command=write_data)
    button_3 = Button(text="Закрыть форму", activebackground='red', highlightcolor='red', bg='blue', fg='white',
                      command=exit_form)
    button_1.grid(row=3, column=1, padx=30, pady=20, sticky='nesw')
    button_2.grid(row=4, column=1, padx=30, pady=20, sticky='nesw')
    button_3.grid(row=5, column=1, padx=30, pady=20, sticky='nesw')
    speaker_text(text_2 + text_1)

    window.mainloop()


if __name__ == "__main__":
    main_form()
