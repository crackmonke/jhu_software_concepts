from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

# Url to scape - does not include the page number by itself
url = "https://www.thegradcafe.com/survey/?page="
pattern = r'/result/\d+'

def get_links():
    page_number = 1
    all_links = set()

    while True:
        try:
            current_url = f"{url}{page_number}"
            page = urlopen(current_url)
            html = page.read().decode('utf-8')
        except:
            break

    return all_links
