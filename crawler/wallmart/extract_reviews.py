from bs4 import BeautifulSoup
import requests
from crawler.utils import get
import json

url_template = 'https://www.walmart.com/search/?cat_id=0&page={}&ps=40&query=fiber+supplement&typeahead=fiber+su#searchProductResult'

config = {
}


def get_review(primary_id, pg, rating):
    print("\t\tPage:{} ".format(pg))
    url = "https://www.walmart.com/terra-firma/fetch"

    querystring = {"rgs": "REVIEWS_MAP"}

    payload = {
        'itemId': primary_id, 'paginationContext':
            {
                'page': pg,
                'sort': 'rating-asc' if rating else 'relevancy',
                'filters': ["rating:eq:{}".format(rating)] if rating else [],
                'limit': 20,
            }
    }

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        # 'Postman-Token': "55d8567a-8e32-4f6d-94d1-3a44d04d6b6e"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, params=querystring)

    return response.json()



def get_reviews(url, rating):
    source = get(url)
    bid = source.find('"primaryProduct":"')
    bid2 = source.find('","', bid + 1)
    primary_id = source[bid + 18: bid2]
    reviews = []

    def add(rs):
        for review in rs:
            reviews.append({
                'author': {
                    'name': review.get('userNickname'),
                },
                'review_title': review.get('reviewTitle'),
                'rating': review.get('rating'),
                'date': review.get('reviewSubmissionTime'),
                'review_data': review.get('reviewText'),
            })
    try:
        rsp = get_review(primary_id, 1, rating)
        rev = rsp["payload"]["reviews"][primary_id]["customerReviews"]
        add(rev)

        pages = rsp["payload"]["reviews"][primary_id]["pagination"]["pages"]

        if pages and len(pages) > 1:
            total_to_go = pages[-1]["num"]
            print("\t\tTOTAL ESTIMATED PAGES: {} REVIEWS: {}".format(total_to_go, total_to_go * 20))
            for pg in range(2, total_to_go + 1):
                try:
                    rsp = get_review(primary_id, pg, rating)
                    rev = rsp["payload"]["reviews"][primary_id]["customerReviews"]
                    add(rev)
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
    return reviews


products = []
done = {}
for pg in range(0, 16):
    print("Page: {}".format(pg))
    data = get(url_template.format(pg + 1))

    soup = BeautifulSoup(data)
    items = soup.findAll('div', class_='search-result-gridview-item')
    for each_item in items:
        pr = each_item.find('a', class_='product-title-link')
        if pr:
            url = "https://www.walmart.com{}".format(pr['href'])
            if url in done:
                continue
            done[url] = ""
            print("\t{}".format(url))
            name = pr['aria-label']
            name = name.strip()
            print("\t{}".format(name))
            if name[0] == '(':
                r = name.find(')')
                name = name[r + 1:]
                name = name.strip()
            price = None
            price_comp = each_item.find('span', class_='price-group')
            if price_comp:
                price = price_comp['aria-label']

            splt = name.split(" ")
            if len(splt) > 2 and splt[1].lower() == 'pack':
                if splt[2] == '-':
                    splt = splt[3:]
                else:
                    splt =  splt[2:]

            brand_name = splt[0].lower()

            if 'benefiber' in name.lower():
                brand_name = 'benefiber'
            elif 'metamucil' in name.lower():
                brand_name = 'metamucil'
            elif 'Vitamin Shoppe Miracle'.lower() in name.lower():
                brand_name = 'Vitamin Shoppe Miracle'

            if 'phillips' in brand_name.lower():
                brand_name  =  'phillips'


            print("\tBrand Name:{}".format(brand_name))
            l = url.rfind('/')
            product_id = url[l + 1:]
            product_review_url = "https://www.walmart.com/reviews/product/{}".format(product_id)
            reviews = get_reviews(product_review_url, None)
            # reviews += get_reviews(product_review_url, 4)
            # reviews += get_reviews(product_review_url, 3)
            # reviews += get_reviews(product_review_url, 2)
            # reviews += get_reviews(product_review_url, 1)
            print("\tReviews: {}".format(len(reviews)))

            prev_brand_data = config.get(brand_name, {})
            prev_brand_data[name] = {
                'url': url,
                'reviews': reviews,
            }
            config[brand_name] = prev_brand_data


ns = {}
ns['wallmart'] = config
config = ns

import json

f = open('wallmart.json', "w+")
f.write(json.dumps(config))
