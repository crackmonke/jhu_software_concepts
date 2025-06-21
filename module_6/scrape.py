"""Module for scraping and saving application data from TheGradCafe."""

import re
import json
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from clean import clean_data

URL = "https://www.thegradcafe.com/survey/?page="

def parse_group(group):
    """Parse a single group row and return a data dictionary with all expected fields."""
    data = {
        'school_name': None,
        'program': None,
        'degree': None,
        'date_added': None,
        'decision': None,
        'result_url': None,
        'semester_year': None,
        'international_american': None,
        'gpa': None,
        'gre_v_score': None,
        'gre_aw': None,
        'gre_score': None,
        'comment': None
    }
    school_div = group.find(
        'div',
        class_='tw-font-medium tw-text-gray-900 tw-text-sm'
    )
    if school_div:
        data['school_name'] = school_div.get_text(strip=True)

    program_td = group.find_all('td')[1] if len(group.find_all('td')) > 1 else None
    if program_td:
        program_div = program_td.find('div', class_='tw-text-gray-900')
        if program_div:
            spans = program_div.find_all('span')
            if len(spans) > 0:
                data['program'] = spans[0].get_text(strip=True)
            degree_span = program_div.find_next('span', class_='tw-text-gray-500')
            if degree_span:
                data['degree'] = degree_span.get_text(strip=True)

    tds = group.find_all('td')
    if len(tds) >= 3:
        data['date_added'] = tds[2].get_text(strip=True)

    decision_div = group.find('div', class_=re.compile(r'tw-inline-flex.*'))
    if decision_div:
        data['decision'] = decision_div.get_text(strip=True)

    result_link = group.find('a', href=re.compile(r'^/result/\d+'))
    if result_link:
        data['result_url'] = f"https://www.thegradcafe.com{result_link['href']}"

    return data

def parse_below_td(below_td, data):
    """Parse the below_td row for tags and comments, always setting all expected fields."""
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
    return data

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
            data = parse_group(group)
            below_td = group.find_next_sibling('tr')
            data = parse_below_td(below_td, data)
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
    return None  # Ensure a return value in all cases

if __name__ == "__main__":
    DATA = scrape_data(max_pages=1000)
    CLEANED_DATA = clean_data(DATA)
    save_data(CLEANED_DATA)

    USER_INPUT = input("Would you like to print the loaded data? (y/n): ").strip().lower()
    PRINT_ENTRIES = USER_INPUT == 'y'
    load_data(print_entries=PRINT_ENTRIES)
