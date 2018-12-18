from crawler.amazon import amazon

keyword = 'fiber supplements'

product_data = amazon.get_data(keyword=keyword, domain='co.uk', max_products=2)

file_name = "{}.json".format(keyword.replace(' ', '_').lower().strip())

import json
f = open(file_name, "w+")
f.write(json.dumps(product_data))