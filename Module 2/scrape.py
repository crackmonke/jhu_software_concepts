from bs4 import BeautifulSoup
from urllib.request import urlopen

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

        except:
            break

        # grab groupings of data
        groups = data_table.find_all('tr', class_=False)

        for group in groups:
            print(f"Processing group: {group}")
            data = {}

            # School Name
            school_name = group.find('td', class_='tw-font-medium tw-text-gray-900 tw-text-sm')
            if school_name:
                data['school_name'] = school_name.get_text(strip=True)
            else:
                data['school_name'] = None

            # Program Name
            program_name = group.find('td', class_='tw-text-gray-900')
            if program_name:
                data['program_name'] = program_name.get_text(strip=True)
            else:
                data['program_name'] = None

            if data['program_name'] or data['school_name']:
                collected_data.append(data)

        # Move to the next page
        page_number += 1

    return collected_data

entries = scrape_data(3)
for entry in entries:
    print(entry)