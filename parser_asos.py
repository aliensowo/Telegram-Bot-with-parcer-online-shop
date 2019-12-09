import requests
import csv
from bs4 import BeautifulSoup as BS

header = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

base_url_s = 'https://www.asos.com/ru/men/ctas/aktsiya-8/cat/?cid=28240&ctaref=shop|50offparty|mw_hp_50&page=1'
items = []

def s_parse(base_url_s, header):

    session = requests.Session()
    request = session.get(base_url_s, headers=header)
    if request.status_code == 200:
        soup = BS(request.content, 'html.parser')
        divs = soup.find_all('article', attrs={'data-auto-id': 'productTile'})
        for div in divs:
            #brand = div.find('strong', attrs={'class': 'brand-name'}).text
            title = div.find('div', attrs={'data-auto-id': 'productTileDescription'}).text
            new_price = div.find('span', attrs={'data-auto-id': 'productTileSaleAmount'}).text
            old_price = div.find('span', attrs={'data-auto-id': 'productTilePrice'}).text
            #currency = div.find('span', attrs={'class': 'price__currency'}).text
            items.append({
                'title': title,
                'new price': new_price,
                'old prise and sale': old_price,

            })
            print(title)
            print(old_price)
            print(new_price)
            print("*")
            #print(items)

    else:
        print('ERROR')
    return items


def file_writer(items):
    with open('parser_items.csv', 'a',  encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Название', 'Старая цена', 'Новая цена'))
        for item in items:
            a_pen.writerow((item['title'], item['new price'], item['old prise and sale']))

s_parse(base_url_s,header)


file_writer(items)