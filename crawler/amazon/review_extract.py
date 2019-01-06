from crawler.utils import get
from bs4 import BeautifulSoup


def get_review(url, title=None):
    output = []
    end_index = url.rfind('/dp/')
    ar = url[0: end_index]
    ar = ar[0: ar.rfind('/') + 1]
    review_url = "{}/product-reviews/{}".format(
        'https://amazon.com',
        url[end_index + 4:]
    )

    page_num = 1
    total_reviews = 0
    pp = {}
    stoped = False
    while True:
        review_page_url = "{}?pageNumber={}".format(review_url, page_num)
        soup = BeautifulSoup(get(review_page_url))
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
                try:
                    rating = each_review.find(
                        'a',
                        class_='a-link-normal'
                    )['title'][0]
                except:
                    rating = None

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

                if not auth_name:
                    auth_name = each_review.find('div', class_='a-profile-content')
                    if auth_name:
                        auth_name = auth_name.text
                    else:
                        auth_name = None
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
                key = "{}_{}".format(review_title, review_data)
                if key in pp:
                    stoped =  True
                    break
                pp[key] = {}

            except Exception as e:
                print(e)

        total_reviews += len(reviews)

    print("\t\tTotal Reviews: {}".format(total_reviews))
    return output
