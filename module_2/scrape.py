from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
from clean import clean_data

# Url to scrape - does not include the page number by itself
url = "https://www.thegradcafe.com/survey/?page="

def scrape_data(max_pages=10):
    """
    Scrapes application data from TheGradCafe for a given number of pages.
    Returns a list of dictionaries, each representing an application entry.
    """
    page_number = 1
    collected_data = []

    while page_number <= max_pages:
        print(f"Scraping page {page_number}...")
        try:
            # Build the URL for the current page and parse HTML
            current_url = f"{url}{page_number}"
            soup = BeautifulSoup(urlopen(current_url), 'html.parser')
            data_table = soup.find('table', class_='tw-min-w-full tw-divide-y tw-divide-gray-300')
            if not data_table:
                break  # Stop if no data table is found
        except Exception as e:
            print(f"Failed on page {page_number}: {e}")
            break

        # Find all main rows (each application entry)
        groups = data_table.find_all('tr', class_=False)

        for group in groups:
            data = {}

            # School Name
            school_div = group.find('div', class_='tw-font-medium tw-text-gray-900 tw-text-sm')
            data['school_name'] = school_div.get_text(strip=True) if school_div else None

            # Program + Degree (both are inside the 2nd <td>)
            program_td = group.find_all('td')[1] if len(group.find_all('td')) > 1 else None
            if program_td:
                program_div = program_td.find('div', class_='tw-text-gray-900')
                if program_div:
                    spans = program_div.find_all('span')
                    # First span is program name
                    data['program'] = spans[0].get_text(strip=True) if len(spans) > 0 else None

                    # The next <span> after the program is usually the degree
                    degree_span = program_div.find_next('span', class_='tw-text-gray-500')
                    data['degree'] = degree_span.get_text(strip=True) if degree_span else None
                else:
                    data['program'] = None
                    data['degree'] = None
            else:
                data['program'] = None
                data['degree'] = None

            # Date of Info Added (3rd <td>)
            tds = group.find_all('td')
            data['date_added'] = tds[2].get_text(strip=True) if len(tds) >= 3 else None

            # Decision (e.g., Accepted, Rejected)
            decision_div = group.find('div', class_=re.compile(r'tw-inline-flex.*'))
            data['decision'] = decision_div.get_text(strip=True) if decision_div else None

            # Result URL (link to the result detail)
            result_link = group.find('a', href=re.compile(r'^/result/\d+'))
            data['result_url'] = f"https://www.thegradcafe.com{result_link['href']}" if result_link else None

            # Below td (under tr) - Additional Information
            below_td = group.find_next_sibling('tr')
            if below_td:
                tag_container = below_td.find('div', class_='tw-gap-2 tw-flex tw-flex-wrap')
                if tag_container:
                    tags = tag_container.find_all('div', class_='tw-inline-flex')

                    for tag in tags:
                        text = tag.get_text(strip=True)

                        # Semester/Year (e.g., Fall 2024)
                        if any(season in text.lower() for season in ['fall', 'spring', 'summer']):
                            data['semester_year'] = text
                        
                        # International/American status
                        elif 'international' in text.lower() or 'american' in text.lower():
                            data['international_american'] = text
                        
                        # GPA
                        elif text.lower().startswith('gpa'):
                            data['gpa'] = text.replace('GPA:', '').strip()
                        
                        # GRE Verbal Score
                        elif text.lower().startswith('gre v'):
                            data['gre_v_score'] = text.replace('GRE V:', '').strip()
                        
                        # GRE Analytical Writing
                        elif text.lower().startswith('gre aw'):
                            data['gre_aw'] = text.replace('GRE AW:', '').strip()
                        
                        # GRE General Score
                        elif text.lower().startswith('gre'):
                            data['gre_score'] = text.replace('GRE:', '').strip()

                # Comments (if available)
                comments_row = below_td.find_next_sibling('tr', class_='tw-border-none')
                if comments_row:
                    comment_div = comments_row.find('p', class_='tw-text-gray-500 tw-text-sm tw-my-0')
                    if comment_div:
                        data['comment'] = comment_div.get_text(strip=True)
                    
            # Add the collected entry to the list
            collected_data.append(data)

        page_number += 1

    return collected_data

def save_data(filename='application_data.json'):
    """
    Cleans the scraped data and saves it to a JSON file.
    """
    cleaned_data = clean_data()
    if not cleaned_data:
        print("No valid data to save.")
        return

    # Save the cleaned data to a JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)


data = scrape_data(max_pages=3)  # Adjust the number of pages as needed
cleaned_data = clean_data(data)
save_data(cleaned_data)
