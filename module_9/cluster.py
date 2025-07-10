import pandas as pd

# Load the JSON file
df = pd.read_json('clean_applicant_data.json')

# Count unique program names
unique_programs = df['program_name'].nunique()

print(f"Number of unique program names: {unique_programs}")