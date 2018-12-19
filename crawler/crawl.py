from crawler.amazon import amazon

keyword = 'fiber supplements'

config = {
    'co.uk': {
        'Benefiber': {},
        'Citrucel': {},
        'Garden of Life Raw Fiber': {},
        'Optimum Nutrition': {},
        'Metamucil': {},
        'Yerba': {},
        'Renew Life': {},
        'Now Fiber': {},
    },
    'in': {
        'Benefiber': {},
        'Citrucel': {},
        'Garden of Life Raw Fiber': {},
        'Optimum Nutrition': {},
        'Metamucil': {},
        'Yerba': {},
        'Renew Life': {},
        'Now Fiber': {},
        'Organic India Fiber': {},
    },
    'com': {
        'Benefiber': {},
        'Citrucel': {},
        'Garden of Life Raw Fiber': {},
        'Optimum Nutrition': {},
        'Metamucil': {},
        'Yerba': {},
        'Renew Life': {},
        'Now Fiber': {},
    }
}
responses = {}
for each_domain, domain_keywords in config.items():
    for each_keyword in domain_keywords:
        domain_keywords[each_keyword] = amazon.get_data(
            keyword=keyword,
            domain=each_domain,
            max_page=1
        )


file_name = "{}.json".format(keyword.replace(' ', '_').lower().strip())

import json

f = open(file_name, "w+")
f.write(json.dumps(responses))
