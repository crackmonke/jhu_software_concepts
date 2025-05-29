from scrape import scrape_data

def clean_data():
    data = scrape_data(max_pages=3)  # Adjust the number of pages as needed

    cleaned_data = []
    for entry in data:
        # Skip if any required field is None
        if entry.get('school_name') is None or entry.get('program') is None or entry.get('date_added') is None:
            continue

        # Clean comment field
        comment = entry.get('comment', '')
        if comment is not None:
            comment = comment.replace('\r', ' ').replace('\n', ' ').strip()
            entry['comment'] = comment if comment else None

        cleaned_data.append(entry)

    return cleaned_data


for entry in clean_data():
    print(entry)