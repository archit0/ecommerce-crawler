import requests
import warnings
from bs4 import BeautifulSoup

from .review_extract import get_review
from .questions_extract import get_questions
# Loggers and warning
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# constants
ITEM_CONTAINER = 's-item-container'
PRODUCTS_CLASS_NAME = 's-access-detail-page'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_data(keyword, domain='in', max_page=float("inf"), max_products=float("inf")):
    TEMPLATE_URL = "https://www.amazon.{domain}/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={keyword}&page={page}"

    parsed = {}
    page = 1
    total_products = 0
    while page < max_page and total_products < max_products:
        print('Product Page: {page}'.format(page=page))

        product_page_url = TEMPLATE_URL.format(page=page, keyword=keyword, domain=domain)
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
                    total_products += 1
                    print('\t{title}'.format(title=title))
                    price = each_product.find('span', class_='a-color-price')

                    if price:
                        price = price.text
                        price = price.replace(',', "")
                        price = price.strip()
                        if len(price) > 0:
                            try:
                                int(price[0])
                            except:
                                price = price[1:]


                    parsed[title] = {
                        'reviews': get_review(href, title),
                        'questions': get_questions(href),
                        'price': price,
                    }
            if total_products >= max_products:
                break

        page += 1
    return parsed
