import requests
import logging
import warnings
from bs4 import BeautifulSoup

# Loggers and warning
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# constants
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

products_url = "https://www.myntra.com/web/v2/search/data/wildcraft?f=&p={page}&rows=48"
page = 1
title_dict = {}
f = open("myntra_products.csv", "w+")
while True:
    print(page)
    url = products_url.format(page=page)
    page += 1
    json = requests.get(url, headers=HEADERS).json()
    try:
        length = len(json['data']['results']['products'])
        if length == 0:
            print("OVER")
            break
        for each_product in json['data']['results']['products']:
            href = "https://myntra.com/{}".format(each_product['dre_landing_page_url'])
            title = each_product['product']
            if title not in title_dict:
                f.write("{href}|@|{title}\n".format(title=title, href=href))
                title_dict[title] = True
    except Exception as e:
        print("*"*50)
        print(str(e))
        break
