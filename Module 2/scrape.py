from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Url to scape - does not include the page number by itself
url = "https://www.thegradcafe.com/survey/?page="



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
    collected_data = []

    while page_number <= max_pages:
        print(f"Scraping page {page_number}...")
        try:
            current_url = f"{url}{page_number}"
            soup = BeautifulSoup(urlopen(current_url), 'html.parser')
            data_table = soup.find('table', class_='tw-min-w-full tw-divide-y tw-divide-gray-300')
            if not data_table:
                break
        except Exception as e:
            print(f"Failed on page {page_number}: {e}")
            break

        groups = data_table.find_all('tr', class_=False)

        for group in groups:
            data = {}

            # School Name
            school_div = group.find('div', class_='tw-font-medium tw-text-gray-900 tw-text-sm')
            data['school_name'] = school_div.get_text(strip=True) if school_div else None

            # Program + Degree (2 <span> tags inside div)
            program_block = group.find('div', class_='tw-text-gray-900')
            if program_block:
                spans = program_block.find_all('span')
                data['program'] = spans[0].get_text(strip=True) if len(spans) > 0 else None
                data['degree'] = spans[1].get_text(strip=True) if len(spans) > 1 else None
            else:
                data['program'] = None
                data['degree'] = None

            # Date of Info Added (3rd <td>)
            tds = group.find_all('td')
            data['date_added'] = tds[2].get_text(strip=True) if len(tds) >= 3 else None

            # Decision
            decision_div = group.find('div', class_=re.compile(r'tw-inline-flex.*'))
            data['decision'] = decision_div.get_text(strip=True) if decision_div else None

            # Result URL
            result_link = group.find('a', href=re.compile(r'^/result/\d+'))
            data['result_url'] = f"https://www.thegradcafe.com{result_link['href']}" if result_link else None

            collected_data.append(data)

        page_number += 1

    return collected_data

# Run and print
entries = scrape_data(3)
for entry in entries:
    print(entry)