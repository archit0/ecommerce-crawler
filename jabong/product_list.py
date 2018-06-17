import requests
import logging
import warnings
from bs4 import BeautifulSoup

# Loggers and warning
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# constants
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

products_url = "https://www.jabong.com/wildcraft/find/wildcraft/?q=wildcraft&tt=wi&rank=0&qc=wildcraft&ax=1&page={page}&limit=52&sortField=score&sortBy=desc"
page = 1
title_dict = {}
f = open("jabong_products.csv", "w+")
while True:
    print(page)
    url = products_url.format(page=page)
    print(url)
    page += 1
    data = requests.get(url).text
    soup = BeautifulSoup(data)
    products = soup.findAll('div', class_='product-tile')
    if len(products) <0:
        print("Length over")
        break
    for each_product in products:
        href = "https://www.jabong.com{}".format(each_product.find('a')['href'])
        title = each_product.find('div', class_='h4').text
        f.write("{href}|@|{title}\n".format(title=title, href=href))
        f.flush()
