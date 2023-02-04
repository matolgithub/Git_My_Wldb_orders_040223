from os import getenv
from requests import get
from bs4 import BeautifulSoup as bs
from fake_headers import Headers
from pprint import pprint
from dotenv import load_dotenv
import lxml

load_dotenv()

url = getenv("URL")
headers = Headers().generate()


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
    # print(len(data_goods_list), len(data_price_list), len(data_img_link_list))
    for good_number in range(len(data_goods_list)):
        sku = str(data_goods_list[good_number])[31:-4]
        price_str = str(data_price_list[good_number]).replace("\xa0", "").replace(" ", "")[63:-37]
        price_int = int(str(data_price_list[good_number]).replace("\xa0", "").replace(" ", "")[63:-38])
        link = "https:" + str(data_img_link_list[good_number]).replace(" ", "").replace('"', "")[18:-11]
        total_data_list.append(
            {unit_number: [sku, price_str, price_int, link]})
        unit_number += 1
    pprint(total_data_list)

    return total_data_list


def write_data():
    list_data = read_data()
    num = 1
    not_for_war = [4, 7, 23, 58, 68, 69]
    with open("data_result.xls", "w", encoding="utf-8") as new_file:
        for item in list_data:
            for key, value in item.items():
                result_string = f"{num}:! {value[0]}! {value[1]}! {value[3]}\n{value[2]}"
                if key not in not_for_war and key <= 70:
                    new_file.write(f"{result_string}\n")
                    num += 1


def dialog_func():
    read_data()


def main():
    dialog_func()


if __name__ == "__main__":
    main()
    write_data()
