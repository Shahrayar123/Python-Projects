import requests
from bs4 import BeautifulSoup

def _get_soup_object(url, parser="html.parser"):
    return BeautifulSoup(requests.get(url).text, parser)
