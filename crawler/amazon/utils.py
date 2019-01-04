import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
s = requests.Session()

def reset():
    global s
    s = requests.Session()

from selenium import webdriver

browser = webdriver.Chrome(executable_path='/Users/architdwivedi/Downloads/chromedriver')


def get(url):
    browser.execute_script("window.stop();")
    browser.get(url)
    html_source = browser.page_source
    return html_source