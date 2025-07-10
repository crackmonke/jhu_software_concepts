import pandas as pd

# Load the JSON file
df = pd.read_json('cleaned_applicant_data.json')

# Count unique program names
unique_programs = df['program'].nunique()

print(f"Number of unique programs: {unique_programs}")