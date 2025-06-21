"""Module for scraping and saving application data from TheGradCafe."""

import re
import json
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from clean import clean_data

URL = "https://www.thegradcafe.com/survey/?page="

def scrape_data(max_pages):
    """
    Scrapes application data from TheGradCafe for a given number of pages.
    Returns a list of dictionaries, each representing an application entry.
    Args:
        max_pages (int): Number of pages to scrape.
    Returns:
        list: List of application entries.
    """
    page_number = 1
    collected_data = []

    while page_number <= max_pages:
        print(f"Scraping page {page_number}...")
        try:
            current_url = f"{URL}{page_number}"
            with urlopen(current_url) as response:
                soup = BeautifulSoup(response, 'html.parser')
            data_table = soup.find(
                'table',
                class_='tw-min-w-full tw-divide-y tw-divide-gray-300'
            )
            if not data_table:
                break
        except URLError as exc:
            print(f"Failed on page {page_number}: {exc}")
            break

        groups = data_table.find_all('tr', class_=False)

        for group in groups:
            data = {}

            school_div = group.find(
                'div',
                class_='tw-font-medium tw-text-gray-900 tw-text-sm'
            )
            data['school_name'] = school_div.get_text(strip=True) if school_div else None

            program_td = group.find_all('td')[1] if len(group.find_all('td')) > 1 else None
            if program_td:
                program_div = program_td.find('div', class_='tw-text-gray-900')
                if program_div:
                    spans = program_div.find_all('span')
                    data['program'] = spans[0].get_text(strip=True) if len(spans) > 0 else None
                    degree_span = program_div.find_next('span', class_='tw-text-gray-500')
                    data['degree'] = degree_span.get_text(strip=True) if degree_span else None
                else:
                    data['program'] = None
                    data['degree'] = None
            else:
                data['program'] = None
                data['degree'] = None

            tds = group.find_all('td')
            data['date_added'] = tds[2].get_text(strip=True) if len(tds) >= 3 else None

            decision_div = group.find('div', class_=re.compile(r'tw-inline-flex.*'))
            data['decision'] = decision_div.get_text(strip=True) if decision_div else None

            result_link = group.find('a', href=re.compile(r'^/result/\d+'))
            data['result_url'] = (
                f"https://www.thegradcafe.com{result_link['href']}" if result_link else None
            )

            below_td = group.find_next_sibling('tr')
            if below_td:
                tag_container = below_td.find('div', class_='tw-gap-2 tw-flex tw-flex-wrap')
                if tag_container:
                    tags = tag_container.find_all('div', class_='tw-inline-flex')

                    for tag in tags:
                        text = tag.get_text(strip=True)
                        lower_text = text.lower()

                        if any(season in lower_text for season in ['fall', 'spring', 'summer']):
                            data['semester_year'] = text
                        elif 'international' in lower_text or 'american' in lower_text:
                            data['international_american'] = text
                        elif lower_text.startswith('gpa'):
                            data['gpa'] = text.replace('GPA:', '').strip()
                        elif lower_text.startswith('gre v'):
                            data['gre_v_score'] = text.replace('GRE V:', '').strip()
                        elif lower_text.startswith('gre aw'):
                            data['gre_aw'] = text.replace('GRE AW:', '').strip()
                        elif lower_text.startswith('gre'):
                            data['gre_score'] = text.replace('GRE:', '').strip()

                comments_row = below_td.find_next_sibling('tr', class_='tw-border-none')
                if comments_row:
                    comment_div = comments_row.find(
                        'p',
                        class_='tw-text-gray-500 tw-text-sm tw-my-0'
                    )
                    if comment_div:
                        data['comment'] = comment_div.get_text(strip=True)

            collected_data.append(data)

        page_number += 1

    return collected_data

def save_data(cleaned_data, filename='application_data.json'):
    """
    Saves the cleaned data to a JSON file and prints a summary.
    Args:
        cleaned_data (list): List of cleaned application entries.
        filename (str): Output filename.
    """
    if not cleaned_data:
        print("No valid data to save.")
        return

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(cleaned_data, file, ensure_ascii=False, indent=4)
    print(f"Data was saved to '{filename}' and contains {len(cleaned_data)} entries.")

def load_data(filename='application_data.json', print_entries=False):
    """
    Loads data from a JSON file and optionally prints the data.
    Args:
        filename (str): Input filename.
        print_entries (bool): Whether to print loaded entries.
    Returns:
        list: Loaded data or None if error.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if print_entries:
                print("Loaded data:")
                for entry in data:
                    print(entry)
            return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file '{filename}'.")

if __name__ == "__main__":
    DATA = scrape_data(max_pages=1000)
    CLEANED_DATA = clean_data(DATA)
    save_data(CLEANED_DATA)

    USER_INPUT = input("Would you like to print the loaded data? (y/n): ").strip().lower()
    PRINT_ENTRIES = USER_INPUT == 'y'
    load_data(print_entries=PRINT_ENTRIES)
