import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_review(url, title):
    output = []
    end_index = url.rfind('/dp/')
    review_url = "{}/product-reviews/{}".format(
        url[0: end_index],
        url[end_index + 4:]
    )

    page_num = 1
    total_reviews = 0
    while True:
        review_page_url = "{}?pageNumber={}".format(review_url, page_num)
        soup = BeautifulSoup(
            requests.get(
                review_page_url,
                headers=HEADERS
            ).content
        )
        reviews = soup.findAll('div', class_='review')
        if len(reviews) <= 0:
            break
        print("\t\tPage: {} - Reviews: {}".format(page_num, len(reviews)))
        page_num += 1
        for each_review in reviews:
            try:
                review_title = each_review.find(
                    'a',
                    class_='review-title',
                ).contents[0]

                rating = each_review.find(
                    'a',
                    class_='a-link-normal'
                )['title'][0]

                date = each_review.find(
                    'span',
                    class_='review-date'
                ).contents[0]

                review_data = each_review.find(
                    'span',
                    class_='review-text'
                ).text.replace('\n', ' ')
                auth = each_review.find(
                    'a',
                    class_='author'
                )
                auth_name = None
                auth_profile_url = None
                if auth:
                    auth_name = auth.text
                    auth_profile_url = "https://www.amazon.in{}".format(auth['href'])
                output.append(
                    {
                        'author': {
                            'name': auth_name,
                            'profile_url': auth_profile_url
                        },
                        'title': title,
                        'review_title': review_title,
                        'rating': rating,
                        'date': date,
                        'review_data': review_data,
                    }
                )

            except Exception as e:
                print(e)

        total_reviews += len(reviews)

    print("\t\tTotal Reviews: {}".format(total_reviews))
    return output
