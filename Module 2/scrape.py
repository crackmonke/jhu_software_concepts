from bs4 import BeautifulSoup
from urllib.request import urlopen

# Url to scape - does not include the page number by itself
url = "https://www.thegradcafe.com/survey/?page="

data_table = soup.find('table', class_='tw-min-w-full tw-divide-y tw-divide-gray-300')

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


def scrape_data(max_pages=10):
    page_number = 1

    while page_number <= max_pages:
        print(f"Scraping page {page_number}...")
        try:
            current_url = f"{url}{page_number}"
            page = urlopen(current_url)
            html = page.read().decode('utf-8')

        except:
            break

        # grab groupings of data
        groups = soup.find_all('tr', class_=False)

        for group in groups:
            data = {}


       




