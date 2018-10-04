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

products_url = "https://www.amazon.in/gp/search/ref=sr_pg_1?fst=as%3Aoff&rh=i%3Aaps%2Ck%3Awildcraft%2Cp_89%3AWildcraft&page={page}&keywords=wildcraft&ie=UTF8&qid=1528816582&lo=none"

min_pages = 1
max_pages = 20
f = open("products.csv", "w+")

parsed = {}

for page in range(min_pages, max_pages + 1):
    print('Product Page: {page}'.format(page=page))

    product_page_url = products_url.format(page=page)

    source = requests.get(product_page_url, headers=HEADERS).content
    soup = BeautifulSoup(source)
    all_products = soup.findAll('div', class_=ITEM_CONTAINER)
    for each_product in all_products:
        item = each_product.find('a', class_=PRODUCTS_CLASS_NAME)
        title = item['title']
        print('\t{title}'.format(title=title))
        if not title in parsed:
            href = item['href']
            href = href[0: href.index('/ref')]
            if href.startswith('http'):
                parsed[title] = True
                f.write("{href}|@|{title}\n".format(title=title, href=href))
