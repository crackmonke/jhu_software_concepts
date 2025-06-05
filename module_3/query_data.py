import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="GradCafe",
    user="postgres",
    password="sav"
)
cur = conn.cursor()

# 1. How many entries for Fall 2025?
cur.execute("SELECT COUNT(*) FROM applicant WHERE term ILIKE '%Fall 2025%';")
fall_2024_count = cur.fetchone()[0]
print(f"1. Entries for Fall 2024: {fall_2024_count}")

# 2. Percentage of international students (not American or Other)
cur.execute("SELECT COUNT(*) FROM applicant WHERE us_or_international NOT ILIKE '%American%' AND us_or_international NOT ILIKE '%Other%';")
international_count = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM applicant;")
total_count = cur.fetchone()[0]
percent_international = (international_count / total_count * 100) if total_count else 0
print(f"2. Percentage international: {percent_international:.2f}%")

# 3. Average GPA, GRE, GRE V, GRE AW (where provided)
cur.execute("SELECT AVG(gpa), AVG(gre), AVG(gre_v), AVG(gre_aw) FROM applicant WHERE gpa IS NOT NULL OR gre IS NOT NULL OR gre_v IS NOT NULL OR gre_aw IS NOT NULL;")
avg_gpa, avg_gre, avg_gre_v, avg_gre_aw = cur.fetchone()
print(f"3. Averages (GPA, GRE, GRE V, GRE AW): {avg_gpa}, {avg_gre}, {avg_gre_v}, {avg_gre_aw}")

# 4. Average GPA of American students in Fall 2025
cur.execute("SELECT AVG(gpa) FROM applicant WHERE us_or_international ILIKE '%American%' AND term ILIKE '%Fall 2025%' AND gpa IS NOT NULL;")
avg_gpa_american_fall2024 = cur.fetchone()[0]
print(f"4. Avg GPA of American students in Fall 2024: {avg_gpa_american_fall2024}")

# 5. Percent of Fall 2025 entries that are Acceptances
cur.execute("SELECT COUNT(*) FROM applicant WHERE term ILIKE '%Fall 2025%' AND status ILIKE '%Accept%';")
accept_count = cur.fetchone()[0]
percent_accept = (accept_count / fall_2024_count * 100) if fall_2024_count else 0
print(f"5. Percent Acceptances in Fall 2025: {percent_accept:.2f}%")

# 6. Average GPA of Fall 2025 Acceptances
cur.execute("SELECT AVG(gpa) FROM applicant WHERE term ILIKE '%Fall 2025%' AND status ILIKE '%Accept%' AND gpa IS NOT NULL;")
avg_gpa_accept_fall2024 = cur.fetchone()[0]
print(f"6. Avg GPA of Fall 2025 Acceptances: {avg_gpa_accept_fall2024}")

# 7. Entries for JHU, Masters, Computer Science
cur.execute("SELECT COUNT(*) FROM applicant WHERE program ILIKE '%Johns Hopkins%' AND degree ILIKE '%Master%' AND program ILIKE '%Computer Science%';")
jhu_masters_cs_count = cur.fetchone()[0]
print(f"7. JHU Masters Computer Science entries: {jhu_masters_cs_count}")

cur.close()
conn.close()