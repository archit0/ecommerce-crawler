import sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

from crawler.amazon import amazon
from crawler import utils

config = {
    'co.uk': {
        'Benefiber': {},
        'Metamucil': {},
        'Yerba': {},
        'Now': {},
        'Renew Life': {},
        'Garden of Life': {},
        'Citrucel': {},
        'Optimum Nutrition': {},
        'Vitacost': {},
        'Equate': {},
        'Kirkland': {},
        'Organic India': {},
        'Wellpath': {},
        'Care/Of': {},
        'Baze': {},
        'Zenamins': {},
    },
    # 'in': {
    #     'Benefiber': {},
    #     'Metamucil': {},
    #     'Yerba': {},
    #     'Now': {},
    #     'Renew Life': {},
    #     'Garden of Life': {},
    #     'Citrucel': {},
    #     'Optimum Nutrition': {},
    #     'Vitacost': {},
    #     # 'Equate': {},
    #     # 'Kirkland (Costco)': {},
    #     'Organic India': {},
    #     'Wellpath': {},
    #     # 'Care Of': {},
    #     # 'Baze': {},
    #     # 'Zenamins': {},
    # },
    # 'com': {
    #     'Benefiber': {},
    #     'metamucil': {},
    #     'Yerba': {},
    #     'Now': {},
    #     'Renew Life': {},
    #     'Garden of Life': {},
    #     'Citrucel': {},
    #     'Optimum Nutrition': {},
    #     'Vitacost': {},
    #     'Equate': {},
    #     'Kirkland (Costco)': {},
    #     'Organic India': {},
    #     'Wellpath': {},
    #     'Care/Of': {},
    #     'Baze': {},
    #     'Zenamins': {},
    # }
}

responses = {}
for each_domain, domain_keywords in config.items():
    for each_keyword in domain_keywords:
        utils.reset()
        domain_keywords[each_keyword] = amazon.get_data(
            keyword=each_keyword,
            k2=" husk" if each_keyword == "Organic India" else "fiber supplement",
            domain=each_domain,
            max_page=2
        )

file_name = "{}.json".format('co_uk_quest')

import json

f = open(file_name, "w+")
f.write(json.dumps(config))
