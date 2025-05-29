from scrape import scrape_data

def clean_data():
    data = scrape_data(max_pages=3)  # Adjust the number of pages as needed

    cleaned_data = []
    for entry in data:
        # Skip if any required field is None
        if entry.get('school_name') is None or entry.get('program') is None or entry.get('date_added') is None:
            continue

        # Clean comment field
        if entry.get('comment') is not None:
            comment = entry['comment'].replace('\r', '').replace('\n', '').strip()
            entry['comment'] = comment

        cleaned_data.append(entry)

        

    return cleaned_data


for entry in clean_data():
    print(entry)