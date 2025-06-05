import psycopg2
import json
from datetime import datetime


conn = psycopg2.connect(
    host="localhost",
    database="GradCafe",
    user="postgres",  
    password="sav"  
)

cur = conn.cursor()

def parse_float(val):
    try:
        if val is None:
            return None
        return float(''.join(c for c in str(val) if c.isdigit() or c == '.'))
    except Exception:
        return None

with open(r'c:\Users\savyg\Documents\jhu_software_concepts\module_2\application_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    # Only insert if required fields are present
    if 'school_name' in item and 'program' in item and 'degree' in item and 'date_added' in item and \
       'decision' in item and 'result_url' in item and 'semester_year' in item and 'international_american' in item:
        program = f"{item['school_name']} - {item['program']}"
        degree = item['degree']
        try:
            date_added = datetime.strptime(item['date_added'], '%b %d, %Y').date()
        except Exception:
            date_added = None
        status = item['decision']
        url = item['result_url']
        term = item['semester_year']
        us_or_international = item['international_american']
        gpa = parse_float(item.get('gpa'))
        gre_v = parse_float(item.get('gre_v_score'))
        gre_aw = parse_float(item.get('gre_aw'))
        gre = parse_float(item.get('gre_score'))
        comments = item.get('comment')

        cur.execute(
            """
            INSERT INTO applicant
            (program, degree, date_added, status, url, term, us_or_international, gpa, gre_v, gre_aw, gre, comments)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (program, degree, date_added, status, url, term, us_or_international, gpa, gre_v, gre_aw, gre, comments)
        )

conn.commit()
cur.close()
conn.close()