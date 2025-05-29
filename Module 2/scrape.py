from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

# Url to scape - does not include the page number by itself
url = "https://www.thegradcafe.com/survey/?page="
pattern = r'/result/\d+'

def get_links(max_pages=10):
    page_number = 1
    all_links = set()

    while page_number <= max_pages:
        print(f"Scraping page {page_number}...")
        try:
            current_url = f"{url}{page_number}"
            page = urlopen(current_url)
            html = page.read().decode('utf-8')
        except:
            break

        links = re.findall(pattern, html)
        if not links:
            break

        for link in links:
            all_links.add(link)

        page_number += 1

    print(all_links)

get_links()