"""Query statistics from the GradCafe applicant database and generate a PDF report."""

import psycopg2
from fpdf import FPDF

HOST = "localhost"
DATABASE = "GradCafe"
USERNAME = "postgres"
PASSWORD = "sav"

conn = psycopg2.connect(
    host=HOST,
    database=DATABASE,
    user=USERNAME,
    password=PASSWORD
)
cur = conn.cursor()

# 1. How many entries for Fall 2025?
cur.execute(
    "SELECT COUNT(*) FROM applicant WHERE term ILIKE '%Fall 2025%';"
)
fall_2025_count = cur.fetchall()[0][0]
print(f"1. Entries for Fall 2025: {fall_2025_count}")

# 2. Percentage of international students (not American)
cur.execute(
    "SELECT COUNT(*) FROM applicant WHERE us_or_international ILIKE '%International%';"
)
international_count = cur.fetchall()[0][0]
cur.execute("SELECT COUNT(*) FROM applicant;")
total_count = cur.fetchall()[0][0]
percent_international = (international_count / total_count * 100) if total_count else 0
print(f"2. Percentage international: {percent_international:.2f}%")

# 3. Average GPA, GRE, GRE V, GRE AW (where provided)
cur.execute(
    "SELECT AVG(gpa), AVG(gre), AVG(gre_v), AVG(gre_aw) "
    "FROM applicant WHERE gpa IS NOT NULL OR gre IS NOT NULL "
    "OR gre_v IS NOT NULL OR gre_aw IS NOT NULL;"
)
avg_gpa, avg_gre, avg_gre_v, avg_gre_aw = cur.fetchall()[0]
print(
    f"3. Averages (GPA, GRE, GRE V, GRE AW): "
    f"{avg_gpa}, {avg_gre}, {avg_gre_v}, {avg_gre_aw}"
)

# 4. Average GPA of American students in Fall 2025
cur.execute(
    "SELECT AVG(gpa) FROM applicant "
    "WHERE us_or_international ILIKE '%American%' "
    "AND term ILIKE '%Fall 2025%' AND gpa IS NOT NULL;"
)
avg_gpa_american_fall2025 = cur.fetchall()[0][0]
print(f"4. Avg GPA of American students in Fall 2025: {avg_gpa_american_fall2025}")

# 5. Percent of Fall 2025 entries that are Acceptances
cur.execute(
    "SELECT COUNT(*) FROM applicant "
    "WHERE term ILIKE '%Fall 2025%' AND status ILIKE '%Accept%';"
)
accept_count = cur.fetchall()[0][0]
percent_accept = (accept_count / fall_2025_count * 100) if fall_2025_count else 0
print(f"5. Percent Acceptances in Fall 2025: {percent_accept:.2f}%")

# 6. Average GPA of Fall 2025 Acceptances
cur.execute(
    "SELECT AVG(gpa) FROM applicant "
    "WHERE term ILIKE '%Fall 2025%' AND status ILIKE '%Accept%' AND gpa IS NOT NULL;"
)
avg_gpa_accept_fall2025 = cur.fetchall()[0][0]
print(f"6. Avg GPA of Fall 2025 Acceptances: {avg_gpa_accept_fall2025}")

# 7. Entries for JHU, Masters, Computer Science
cur.execute(
    "SELECT COUNT(*) FROM applicant "
    "WHERE program ILIKE '%Johns Hopkins%' "
    "AND degree ILIKE '%Master%' "
    "AND program ILIKE '%Computer Science%';"
)
jhu_masters_cs_count = cur.fetchall()[0][0]
print(f"7. JHU Masters Computer Science entries: {jhu_masters_cs_count}")

# Prepare Q&A for PDF
qa = [
    (
        "1. How many entries do you have in your database who have applied for Fall 2025?",
        f"{fall_2025_count}"
    ),
    (
        "2. What percentage of entries are from international students (not American)? "
        "(to two decimal places)",
        f"{percent_international:.2f}%"
    ),
    (
        "3. What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?",
        f"GPA: {avg_gpa}, GRE: {avg_gre}, GRE V: {avg_gre_v}, GRE AW: {avg_gre_aw}"
    ),
    (
        "4. What is their average GPA of American students in Fall 2025?",
        f"{avg_gpa_american_fall2025}"
    ),
    (
        "5. What percent of entries for Fall 2025 are Acceptances (to two decimal places)?",
        f"{percent_accept:.2f}%"
    ),
    (
        "6. What is the average GPA of applicants who applied for Fall 2025 who are Acceptances?",
        f"{avg_gpa_accept_fall2025}"
    ),
    (
        "7. How many entries are from applicants who applied to JHU for a masters degrees in "
        "Computer Science?",
        f"{jhu_masters_cs_count}"
    )
]

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "GradCafe Database Query Results", ln=True, align='C')
pdf.ln(5)

# Add description of the query and why
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Description of Query and Purpose:", ln=True)
pdf.set_font("Arial", size=12)
DESCRIPTION = (
    "This report summarizes key statistics from the GradCafe applicant database for Fall 2025. "
    "The queries were designed to answer specific questions about the applicant pool, including "
    "the number of entries, percentage of international students, average academic metrics, and "
    "details about specific subgroups such as American applicants, acceptances, and those applying "
    "to JHU for a master's in Computer Science. The purpose is to provide a data-driven overview "
    "of the application trends and outcomes for this admissions cycle."
)
pdf.multi_cell(0, 10, DESCRIPTION)
pdf.ln(5)

for question, answer in qa:
    pdf.multi_cell(0, 10, f"Q: {question}\nA: {answer}", align='L')
    pdf.ln(2)

pdf.output("query_results.pdf")

cur.close()
conn.close()