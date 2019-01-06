import requests
import logging
import warnings
from bs4 import BeautifulSoup

# Loggers and warning
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# constants
ITEM_CONTAINER = 's-item-container'
PRODUCTS_CLASS_NAME = 's-access-detail-page'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

products_url = "https://www.flipkart.com/search?q=fiber%20supplement&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}"

f = open("products.csv", "w+")

parsed = {}
page = 1
while True:

    print('Product Page: {page}'.format(page=page))
    product_page_url = products_url.format(page=page)
    page += 1
    source = requests.get(product_page_url, headers=HEADERS).content
    soup = BeautifulSoup(source)
    rows = soup.findAll('div', class_='_3O0U0u')
    if len(rows) == 0:
        break
    for each_row in rows:
        for each_product in each_row.children:
            ele = each_product.findAll('a')[1]
            href = 'https://www.flipkart.com{}'.format(ele['href'])
            title = ele.text
            f.write("{href}|@|{title}\n".format(title=title, href=href))
