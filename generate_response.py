"""
Генерируем до 5 блоков, в каждом блоке до 5 элементов.

title: заголовок блока - до 200 символов
quote: цитата - до 300 символов
img: ссылка на картинку - до 200 символов
text: текст блока - до 1000 символов
button: кнопка - до 100 символов
Элементы должны идти в случайном порядке, кнопки могут встречаться в любом месте. 
Каждый элемент имеет параметр "item_severity" — уровень важности (например, 1 — самый важный).
"""



import random
from typing import List, Dict, Any


def generate_random_title() -> str:
    return "Заголовок " + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ', k=random.randint(10, 200)))

def generate_random_text() -> str:
    return "Текст блока " + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ', k=random.randint(50, 1000)))

def generate_random_quote() -> str:
    return "Цитата " + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ', k=random.randint(20, 300)))

def generate_random_button() -> str:
    return "Кнопка " + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ', k=random.randint(5, 100)))


def generate_response() -> List[Dict[str, Any]]:
    response = []
    num_blocks = random.randint(1, 5)  

    for block_id in range(num_blocks):
        block_items = []
        num_items = random.randint(1, 5)  

        for item_id in range(num_items):
            item_type = random.choice(['title', 'text', 'quote', 'img', 'button'])
            item_severity = random.randint(1, 2)  

            if item_type == 'title':
                item = {
                    'item_type': 'title',
                    'item_data': generate_random_title(),
                    'item_severity': item_severity
                }
            elif item_type == 'text':
                item = {
                    'item_type': 'text',
                    'item_data': generate_random_text(),
                    'severity': item_severity
                }
            elif item_type == 'quote':
                item = {
                    'item_type': 'quote',
                    'item_data': generate_random_quote(),
                    'item_link': random.choice(links),
                    'severity': item_severity
                }
            elif item_type == 'img':
                item = {
                    'item_type': 'img',
                    'item_data': random.choice(links),
                    'severity': item_severity
                }
            elif item_type == 'button':
                item = {
                    'item_type': 'button',
                    'item_data': generate_random_button(),
                    'severity': item_severity
                }

            block_items.append(item)

        response.append(block_items)

    return response

links = [
    "https://ds56-glazov-r18.gosweb.gosuslugi.ru/nash-detskiy-sad/novosti-i-sobytiya/perehodim-dorogu-bezopasno.html", 
    "https://sh10-sokol-r19.gosweb.gosuslugi.ru/netcat_files/userfiles/169298a6-c767-47b4-b5ce-9de17ffcab87.jpg",
    "https://ds56-glazov-r18.gosweb.gosuslugi.ru/nash-detskiy-sad/novosti-i-sobytiya/perehodim-dorogu-bezopasno.html",
    "https://semenov.nobl.ru/presscenter/news/134742/?ysclid=mcugheu2pr707528320",
    "https://schools20mogilev.by/%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%BA%D0%B0%D0%BC/%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D1%8B%D0%B5-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8/%D0%BE%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D0%BE-%D0%B4%D0%BE%D1%80%D0%BE%D0%B3%D0%B0?ysclid=mcugineuu0249384163",
    "https://ds56-glazov-r18.gosweb.gosuslugi.ru/nash-detskiy-sad/novosti-i-sobytiya/perehodim-dorogu-bezopasno.html", 
    "https://sh10-sokol-r19.gosweb.gosuslugi.ru/netcat_files/userfiles/169298a6-c767-47b4-b5ce-9de17ffcab87.jpg", 
    "https://ds56-glazov-r18.gosweb.gosuslugi.ru/nash-detskiy-sad/novosti-i-sobytiya/perehodim-dorogu-bezopasno.html",
    "https://schools20mogilev.by/%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%BA%D0%B0%D0%BC/%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D1%8B%D0%B5-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8/%D0%BE%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D0%BE-%D0%B4%D0%BE%D1%80%D0%BE%D0%B3%D0%B0?ysclid=mcugineuu0249384163",
    "https://sh10-sokol-r19.gosweb.gosuslugi.ru/netcat_files/userfiles/169298a6-c767-47b4-b5ce-9de17ffcab87.jpg", 
    "https://i.pinimg.com/736x/17/99/b9/1799b951d47f835086c556d1011a96bf.jpg" ,
    "https://present5.com/presentation/1/63698357_336320975.pdf-img/63698357_336320975.pdf-10.jpg", 

]


if __name__ == "__main__":
    generated_response = generate_response()
    for block in generated_response:
        print(block)