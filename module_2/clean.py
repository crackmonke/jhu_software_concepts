from scrape import scrape_data
import json

def clean_data():
    data = scrape_data(max_pages=3)  # Adjust the number of pages as needed

    cleaned_data = []
    for entry in data:
        # Skip if any required field is None
        if entry.get('school_name') is None or entry.get('program') is None or entry.get('date_added') is None:
            continue

        # Clean all string fields: strip whitespace
        for key, value in entry.items():
            if isinstance(value, str):
                entry[key] = value.strip()

        # Clean comment field: remove \r and \n
        if entry.get('comment') is not None:
            entry['comment'] = entry['comment'].replace('\r', '').replace('\n', '').strip()

        cleaned_data.append(entry)

    return cleaned_data

def save_data(filename='application_data.json'):
    cleaned_data = clean_data()
    if not cleaned_data:
        print("No valid data to save.")
        return

    # Save the cleaned data to a JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)