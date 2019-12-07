import requests
from bs4 import BeautifulSoup as BS

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

base_url = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?pagesize=40&sort=sale'


def wb_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = BS(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'dtList i-dtList j-card-item'})
        for div in divs:
            brand = div.find('strong', attrs={'class': 'brand-name'}).text
            title = div.find('span', attrs={'class': 'goods-name'}).text
            new_price = div.find('ins', attrs={'class': 'lower-price'}).text
            old_price = div.find('span', attrs={'class': 'price-old-block'}).text
            print(brand.upper())
            print(title)
            print(old_price)
            print(new_price)
            print("*")

    else:
        print('ERROR')


wb_parse(base_url, headers)