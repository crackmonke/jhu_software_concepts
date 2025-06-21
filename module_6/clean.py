"""Module for cleaning scraped application data."""

import re

def clean_data(data):
    """
    Cleans a list of application entries.
    Strips whitespace and normalizes comments.
    Args:
        data (list): List of dictionaries representing application entries.
    Returns:
        list: Cleaned list of application entries.
    """
    cleaned_data = []
    for entry in data:
        if entry.get('school_name') is None or entry.get('program') is None or \
           entry.get('date_added') is None:
            continue

        for key, value in entry.items():
            if isinstance(value, str):
                entry[key] = value.strip()

        if entry.get('comment') is not None:
            comment = re.sub(r'[\r\n]+', ' ', entry['comment'])
            comment = re.sub(r'\s+', ' ', comment).strip()
            entry['comment'] = comment

        cleaned_data.append(entry)

    return cleaned_data
