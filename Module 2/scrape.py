from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

url = "https://www.thegradcafe.com/survey/"

page = urlopen(url)
html = page.read().decode("utf-8")

pattern = r'/results/\d+'

def scrape_data():
    links = re.findall(pattern, html)

    print("Found links:")
    for link in links:
        print(link) 

scrape_data()
