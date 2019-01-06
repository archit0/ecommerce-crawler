from bs4 import BeautifulSoup
import requests
from crawler.utils import get

url = 'https://www.vitacost.com/productResults.aspx?N=0&Ntt=fiber+supplement&No={}'

products = []
for pg in range(0, 301, 20):
    u = url.format(pg)
    data = get(u)

    soup = BeautifulSoup(data)
    pr = soup.findAll('a', class_='ellipsis60')
    for e in pr:
        ur = "https://www.vitacost.com{}".format(e['href'])
        products.append(ur)
        print(ur)



def get_response(id, offset):
    url = "https://api.bazaarvoice.com/data/batch.json"

    querystring = {

        "passkey": "pgtdnhg3w0npen2to8bo3bbqn",
        "apiversion": "5.5",
        "displaycode": "4595-en_us",
        "resource.q0": "reviews",
        "filter.q0": [
            "isratingsonly:eq:false",
            "productid:eq:{}".format(id),
            "contentlocale:eq:en_US"
        ],
        "sort.q0": "relevancy:a1",
        "stats.q0": "reviews",
        "filteredstats.q0": "reviews",
        "include.q0": "authors,products,comments",
        "filter_reviews.q0": "contentlocale:eq:en_US",
        "filter_reviewcomments.q0": "contentlocale:eq:en_US",
        "filter_comments.q0": "contentlocale:eq:en_US",
        "offset.q0": str(offset)
    }
    headers = {
        # 'Referer': "https://www.vitacost.com/vitacost-triple-fiber",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'cache-control': "no-cache",
        # 'Postman-Token': "93034291-5834-4534-9513-102517dde314"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

config = {
    'vitacost': {}
}
count = 0
for each_product in products:
    try:
        last_slash = each_product.rfind('/')
        first_hyp = each_product.find('-')
        brand_name = each_product[last_slash + 1: first_hyp]

        source = get(each_product)
        bid = source.find('''$BV.configure('global', { productId : "''')
        bid2 = source.find('" }', bid + 1)
        each_id = source[bid + 39: bid2]

        offset = 0

        print("Id: {}".format(each_id))


        def parse_review(reviews):
            rt = []
            for review in reviews:
                rt.append({
                    'author': {
                        'name': review['UserNickname'],
                        'location': review['UserLocation'],
                        'profile_url': None
                    },
                    'review_title': review['Title'],
                    'rating': review['Rating'],
                    'date': review['SubmissionTime'],
                    'review_data': review['ReviewText'],
                })
            return rt


        response = get_response(each_id, offset)
        product_name = response['BatchedResults']['q0']['Includes']['Products'][each_id]['Name']
        url = response['BatchedResults']['q0']['Includes']['Products'][each_id]['ProductPageUrl']
        reviews = parse_review(response['BatchedResults']['q0']['Results'])
        max_offset = response['BatchedResults']['q0']['TotalResults']

        while offset <= max_offset:
            print("\tOffset: {}".format(offset))
            offset += 10
            response = get_response(each_id, offset)
            reviews += parse_review(response['BatchedResults']['q0']['Results'])

        output = {
            'url': url,
            'reviews': reviews,
        }


        brand_data = config['vitacost'].get(brand_name, {})
        brand_data[product_name] = output
        config['vitacost'][brand_name] = brand_data
    except Exception as e:
        print(e, "No reviews", each_product)


import json

f = open('vitacost.json', "w+")
f.write(json.dumps(config))