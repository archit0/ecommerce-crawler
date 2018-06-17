import requests
import warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

with open("products.csv") as data:
    content = data.read().split('\n')

f = open("reviews.csv", "w+")

for row in content:
    sp = row.split('|@|')
    if len(sp) == 2:
        url, title = sp
        end_index = url.rfind('&lid=')
        review_url = url[0: end_index].replace('/p/', '/product-reviews/')
        print("Extracting reviews for: {}".format(title))
        page_num = 1
        total_reviews = 0
        while True:
            review_page_url = "{}&page={}".format(review_url, page_num)
            soup = BeautifulSoup(
                requests.get(
                    review_page_url,
                    headers=HEADERS
                ).content
            )

            reviews = soup.findAll('div', class_='_3DCdKt')
            if len(reviews) <= 0:
                break
            print("\tPage: {} - Reviews: {}".format(page_num, len(reviews)))
            page_num += 1
            for each_review in reviews:
                try:
                    review_title = each_review.find(
                        'p',
                        class_='_2xg6Ul',
                    ).text

                    rating = each_review.find(
                        'div',
                        class_='E_uFuv'
                    ).text[0]

                    date = each_review.findAll(
                        'p',
                        class_='_3LYOAd'
                    )[1].text
                    review_data = each_review.find(
                        'div',
                        class_='qwjRop'
                    ).text.replace('\n', ' ').replace('READ MORE', '')

                    f.write(
                        "{}|@|{}|@|{}|@|{}|@|{}\n".format(
                            title,
                            review_title,
                            rating,
                            date,
                            review_data
                        )
                    )
                    f.flush()

                except Exception as e:
                    print(e)

            total_reviews += len(reviews)

        print("\tTotal Reviews: {}".format(total_reviews))
