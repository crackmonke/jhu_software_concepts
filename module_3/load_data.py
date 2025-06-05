import psycopg2
import json
from datetime import datetime


# Prompt for PostgreSQL username and password, with defaults
host = "localhost"
database = "GradCafe"
def_username = "postgres"

username = input(f"Enter PostgreSQL username (default: {def_username}): ") or def_username
password = input("Enter PostgreSQL password: ")

conn = psycopg2.connect(
    host=host,
    database=database,
    user=username,
    password=password
)

cur = conn.cursor()

# Create the applicant table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS applicant (
        p_id SERIAL PRIMARY KEY, -- Unique identifier
        program TEXT,           -- University and Department
        comments TEXT,          -- Comments
        date_added DATE,        -- Date Added
        url TEXT,               -- Link to Post on Grad Café
        status TEXT,            -- Admission Status
        term TEXT,              -- Start Term
        us_or_international TEXT, -- Student nationality
        gpa FLOAT,              -- Student GPA
        gre FLOAT,              -- Student GRE Quant
        gre_v FLOAT,            -- Student GRE Verbal
        gre_aw FLOAT,           -- Student Average Writing
        degree TEXT             -- Student Program Degree Type
    );
''')

# Add column descriptions (PostgreSQL COMMENT statements)
cur.execute("""
    COMMENT ON COLUMN applicant.p_id IS 'Unique identifier';
    COMMENT ON COLUMN applicant.program IS 'University and Department';
    COMMENT ON COLUMN applicant.comments IS 'Comments';
    COMMENT ON COLUMN applicant.date_added IS 'Date Added';
    COMMENT ON COLUMN applicant.url IS 'Link to Post on Grad Café';
    COMMENT ON COLUMN applicant.status IS 'Admission Status';
    COMMENT ON COLUMN applicant.term IS 'Start Term';
    COMMENT ON COLUMN applicant.us_or_international IS 'Student nationality';
    COMMENT ON COLUMN applicant.gpa IS 'Student GPA';
    COMMENT ON COLUMN applicant.gre IS 'Student GRE Quant';
    COMMENT ON COLUMN applicant.gre_v IS 'Student GRE Verbal';
    COMMENT ON COLUMN applicant.gre_aw IS 'Student Average Writing';
    COMMENT ON COLUMN applicant.degree IS 'Student Program Degree Type';
""")

def parse_float(val):
    try:
        if val is None:
            return None
        return float(''.join(c for c in str(val) if c.isdigit() or c == '.'))
    except Exception:
        return None

with open('application_data.json', 'r', encoding='utf-8') as f:
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