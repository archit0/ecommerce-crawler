import requests
import warnings
from bs4 import BeautifulSoup

from .review_extract import get_review

# Loggers and warning
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# constants
ITEM_CONTAINER = 's-item-container'
PRODUCTS_CLASS_NAME = 's-access-detail-page'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_data(keyword):
    TEMPLATE_URL = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={keyword}&page={page}"

    parsed = {}
    page = 1

    while True:
        print('Product Page: {page}'.format(page=page))

        product_page_url = TEMPLATE_URL.format(page=page, keyword=keyword)
        print(product_page_url)

        source = requests.get(product_page_url, headers=HEADERS).content
        soup = BeautifulSoup(source)
        all_products = soup.findAll('div', class_=ITEM_CONTAINER)
        if not all_products:
            break
        for each_product in all_products:
            item = each_product.find('a', class_=PRODUCTS_CLASS_NAME)
            if not item:
                continue
            title = item['title']
            if title not in parsed:
                href = item['href']
                href = href[0: href.index('/ref')]
                if href.startswith('http'):
                    print('\t{title}'.format(title=title))
                    price = each_product.find('span', class_='a-color-price')

                    if price:
                        price = price.text
                        price = price.replace(',', "")
                        price = price.strip()
                    reviews = get_review(href, title)

                    parsed[title] = {
                        'reviews': reviews,
                        'price': price,
                    }

        page += 1
    return parsed
