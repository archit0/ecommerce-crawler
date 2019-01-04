import warnings
from bs4 import BeautifulSoup

from .utils import get
from .review_extract import get_review
from .questions_extract import get_questions
# Loggers and warning
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# constants
ITEM_CONTAINER = 's-item-container'
PRODUCTS_CLASS_NAME = 's-access-detail-page'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_data(keyword, k2, domain='in', max_page=float("inf"), max_products=float("inf")):
    TEMPLATE_URL = "https://www.amazon.{domain}/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={keyword}&page={page}"

    parsed = {}
    page = 0
    total_products = 0
    while total_products < max_products:
        page += 1
        if page > max_page:
            break
        print('Product Page: {page}'.format(page=page))

        product_page_url = TEMPLATE_URL.format(page=page, keyword="{} {}".format(keyword, k2), domain=domain)
        print(product_page_url)

        source = get(product_page_url)
        soup = BeautifulSoup(source)
        all_products = soup.findAll('div', class_=ITEM_CONTAINER)

        if not all_products:
            break
        for each_product in all_products:
            try:
                item = each_product.find('a', class_=PRODUCTS_CLASS_NAME)
                if not item:
                    continue
                title = item['title']

                if keyword.lower() not in title.lower() :
                    continue

                if 'fiber' not in title.lower() and 'husk' not in title.lower() and 'fibre' not in title.lower():
                    continue
                if title not in parsed:
                    href = item['href']
                    href = href[0: href.index('/ref')]
                    if href.startswith('http'):
                        total_products += 1
                        print('\t{title}'.format(title=title))

                        parsed[title] = {
                            'reviews': get_review(href, title),
                            'questions': get_questions(href),
                            'price': None,
                        }
                    else:
                        tt = 1
                        b = 1
                        pass
                if total_products >= max_products:
                    break
            except:
                print("Exception occured")
        print("-------------------------------------")
        all_products = soup.findAll('div', class_='desktopSparkle__asinContainer')
        for each_product in all_products:
            try:

                title = each_product.text

                if keyword.lower() not in title.lower():
                    continue

                if 'fiber' not in title.lower() and 'husk' not in title.lower() and 'fibre' not in title.lower():
                    continue
                if title not in parsed:
                    print('\t{title}'.format(title=title))
                    ahr = each_product.find('a')['href']
                    t = ahr.find('/dp/')  + 4
                    q = ahr.find('?', t)
                    id = ahr[t:q]
                    u = "https://amazon.com/{}/dp/{}/ref=sr_1_4_a_it".format(title, id)

                    parsed[title] = {
                        'reviews': get_review(u, title),
                        # 'questions': get_questions(href),
                        'price': None,
                    }
                if total_products >= max_products:
                    break
            except:
                print("Exception occured")
        break
    return parsed
