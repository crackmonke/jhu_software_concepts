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

    return all_links


data_container = soup.find('div', class_='tw-flex tw-flex-col lg:tw-flex-row')
data = data_container.find_all()


def scrape_links():
    links = get_links()





# Program Name
# o University
# o Comments (if available)
# o Date of Informa/on Added to Grad Café
# o URL link to applicant entry
# o Applicant Status
# ▪ If Accepted: Acceptance Date
# ▪ If Rejected: Rejec/on Date
# o Semester and Year of Program Start (if available)
# o Interna/onal / American Student (if available)
# o GRE Score (if available)
# o GRE V Score (if available)
# o Masters or PhD (if available)
# o GPA (if available)
# o GRE AW (if available)