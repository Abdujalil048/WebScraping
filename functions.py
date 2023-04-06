import requests
from bs4 import BeautifulSoup


def get_site(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


