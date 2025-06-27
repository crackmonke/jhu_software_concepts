import re

def clean_data(data):
    expected_fields = [
        'school_name', 'program', 'degree', 'date_added', 'decision',
        'result_url', 'semester_year', 'international_american', 'gpa',
        'gre_v_score', 'gre_aw', 'gre_score', 'comment'
    ]
    cleaned_data = []
    for entry in data:
        # Skip entry if any required field is None
        if entry.get('school_name') is None or entry.get('program') is None or entry.get('date_added') is None:
            continue

        # Ensure all expected fields are present
        for field in expected_fields:
            if field not in entry:
                entry[field] = None

        # Strip whitespace from all string fields in the entry
        for key, value in entry.items():
            if isinstance(value, str):
                entry[key] = value.strip()

        # Clean the comment field by replacing \r and \n with a space, then collapse multiple spaces
        if entry.get('comment') is not None:
            comment = re.sub(r'[\r\n]+', ' ', entry['comment'])
            comment = re.sub(r'\s+', ' ', comment).strip()
            entry['comment'] = comment

        # Add the cleaned entry to the list
        cleaned_data.append(entry)

    # Return the list of cleaned entries
    return cleaned_data

