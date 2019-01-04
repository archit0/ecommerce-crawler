urls = [
    'https://www.hollandandbarrett.json.com/shop/product/holland-barrett-psyllium-husks-capsules-500mg-60018924?skuid=018924',
    'https://www.hollandandbarrett.json.com/shop/product/solgar-psyllium-husks-fibre-500mg-vegi-capsules-60001422?skuid=001422',
    'https://www.hollandandbarrett.json.com/shop/product/holland-barrett-fibre-force-capsules-60013986?skuid=013986',
    'https://www.hollandandbarrett.json.com/shop/product/holland-barrett-colon-care-plus-powder-60004741?skuid=004741',
    'https://www.hollandandbarrett.json.com/shop/product/holland-barrett-mega-potency-acidophilus-capsules-60001540?skuid=001540',
    'https://www.hollandandbarrett.json.com/shop/product/holland-barrett-colon-care-plus-capsules-60018944?skuid=018944',
    'https://www.hollandandbarrett.json.com/shop/product/holland-barrett-regucol-powder-60010180?skuid=010179',
    'https://www.hollandandbarrett.json.com/shop/product/holland-barrett-acai-daily-complex-1000mg-capsules-60029162?skuid=029162',
    'https://www.hollandandbarrett.json.com/shop/product/holland-barrett-yeast-raiders-capsules-60007685?skuid=007685'

]

ids = [
    60018924,
    60001422,
    60013986,
    60004741,
    60001540,
    60018944,
    60010180,
    60029162,
    60007685,
]

import requests


def get_response(id, offset):
    url = "https://api.bazaarvoice.com/data/batch.json"

    querystring = {
        "passkey": "f3visea9f8g42ccsxui8tcale",
        "apiversion": "5.5",
        "displaycode": "3332-en_gb",
        "resource.q0": "reviews",
        "filter.q0": [
            "isratingsonly:eq:false",
            "productid:eq:" + id,
            "contentlocale:eq:en,en_IE,nl_NL,en_GB"
        ],
        "sort.q0": "submissiontime:desc",
        "stats.q0": "reviews",
        "filteredstats.q0": "reviews",
        "include.q0": "authors,products,comments",
        "offset.q0": "{}".format(offset)
    }

    headers = {
        # 'Referer': "https://www.hollandandbarrett.com/shop/product/holland-barrett-psyllium-husks-capsules-500mg-60018924?skuid=018924",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'cache-control': "no-cache",
        # 'Postman-Token': "b6ad0130-efa0-4c5a-8dd3-e099ee1ccac0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


config = {
    'hollandandbarrett.json.com': {
        'hollandandbarrett.json': {

        }
    }
}
for each_id in ids:
    each_id = str(each_id)

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
        'reviews': reviews,
        'url': url,
    }
    config['hollandandbarrett.json.com']['hollandandbarrett.json'][product_name] = output

import json

f = open('hollandandbarrett.json', "w+")
f.write(json.dumps(config))



