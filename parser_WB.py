import requests
from bs4 import BeautifulSoup as BS

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

base_url = 'https://www.wildberries.ru/catalog/premium/muzhchinam?bid=a0d12ae7-2152-4c1b-a4fd-1cfaed91984a'


def lm_parse(base_url, headers):
    items = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = BS(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-type': 'category'})
        for div in divs:
            #brand = div.find('strong', attrs={'class': 'brand-name'}).text
            title = div.find('div', attrs={'class': 'products-list-item__brand'}).text.strip()
            new_price = div.find('span', attrs={'class': 'price__new'}).text
            old_price = div.find('span', attrs={'class': 'price__old'}).text
            currency = div.find('span', attrs={'class': 'price__currency'}).text
            items.append({
                'title': title,
                'new price': new_price,
                'old prise and sale': old_price,
                'currency': currency
            })
            print(title)
            print(old_price)
            print(new_price + ' ' + currency)
            print("*")
            #print(items)

    else:
        print('ERROR')


lm_parse(base_url, headers)