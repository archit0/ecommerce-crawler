import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_questions(href):
    amz_index = href.find('amazon')
    slash = href.find('/', amz_index)
    end  = href.find('/dp/') + 4
    amz = href[0: slash]
    url= "{}/ask/questions/asin/{}/{page}".format(amz, href[end:], page="{page}")

    page  = 1
    output = []
    while True:
        f_url = url.format(page=page)
        soup = BeautifulSoup(
            requests.get(
                f_url,
                headers=HEADERS
            ).content
        )
        print("\t\tPage: {}".format(page))
        questions = soup.find('div', class_='askTeaserQuestions')
        if not questions:
            break
        else:
            found = 0
            for e in list(questions.children):
                if isinstance(e, Tag):
                    quest = e.find('a', class_='a-link-normal')
                    if quest:
                        found += 1
                        quest_text = quest.text.strip()
                        answers = get_answer(amz + quest['href'])
                        print("\t\t\t Total Answers: {} Questions: {} ".format(len(answers), quest_text))
                        output.append({
                            'question': quest_text,
                            'answers': answers
                        })
        print("\t\t\tTotal Questions:  {}".format(found))
        page += 1

    return output

def get_answer(url):

    soup = BeautifulSoup(
        requests.get(
            url,
            headers=HEADERS
        ).content
    )
    response = []
    sections = soup.findAll('div', class_='a-section')
    for each in sections:
        try:
            if each.get('id', None):
                text = each.find('span').text.strip()
                response.append(text)

        except:
            pass
    return response


# print(get_questions('https://www.amazon.co.uk/Solgar-Psyllium-Husks-Vegetable-Capsules/dp/B005P0WGNE'))