"""Load applicant data into the GradCafe PostgreSQL database."""

import json
from datetime import datetime
import psycopg2

HOST = "localhost"
DATABASE = "GradCafe"
DEF_USERNAME = "postgres"

def parse_float(val):
    """Convert value to float or return None if not possible."""
    try:
        if val is None or val == '':
            return None
        return float(''.join(c for c in str(val) if c.isdigit() or c == '.'))
    except ValueError:
        return None

def none_if_empty(val):
    """Return None if value is empty or None."""
    return val if val not in (None, '') else None

def main():
    """Main function to load data into the database."""
    username = input(f"Enter PostgreSQL username (default: {DEF_USERNAME}): ") or DEF_USERNAME
    password = input("Enter PostgreSQL password: ")

    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=username,
        password=password
    )
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS applicant (
            p_id SERIAL PRIMARY KEY,
            program TEXT,
            comments TEXT,
            date_added DATE,
            url TEXT,
            status TEXT,
            term TEXT,
            us_or_international TEXT,
            gpa FLOAT,
            gre FLOAT,
            gre_v FLOAT,
            gre_aw FLOAT,
            degree TEXT
        );
    ''')

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

    with open('application_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        required = [
            'school_name', 'program', 'degree', 'date_added',
            'decision', 'result_url', 'semester_year', 'international_american'
        ]
        if all(field in item for field in required):
            program = none_if_empty(f"{item['school_name']} - {item['program']}")
            degree = none_if_empty(item['degree'])
            try:
                date_added = datetime.strptime(item['date_added'], '%b %d, %Y').date()
            except (ValueError, TypeError):
                date_added = None
            status = none_if_empty(item['decision'])
            url = none_if_empty(item['result_url'])
            term = none_if_empty(item['semester_year'])
            us_or_international = none_if_empty(item['international_american'])
            gpa = parse_float(item.get('gpa'))
            gre_v = parse_float(item.get('gre_v_score'))
            gre_aw = parse_float(item.get('gre_aw'))
            gre = parse_float(item.get('gre_score'))
            comments = none_if_empty(item.get('comment'))

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

if __name__ == "__main__":
    main()