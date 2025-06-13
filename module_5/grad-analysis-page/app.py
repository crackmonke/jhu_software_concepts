from flask import Flask, render_template_string, url_for
import psycopg2

app = Flask(__name__)

def get_query_results():
    conn = psycopg2.connect(
        host="localhost",
        database="GradCafe",
        user="postgres",
        password="sav"
    )
    cur = conn.cursor()

    # 1. How many entries for Fall 2025?
    cur.execute("SELECT COUNT(*) FROM applicant WHERE term ILIKE '%Fall 2025%';")
    fall_2025_count = cur.fetchall()[0][0]

    # 2. Percentage of international students (not American)
    cur.execute("SELECT COUNT(*) FROM applicant WHERE us_or_international ILIKE '%International%';")
    international_count = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM applicant;")
    total_count = cur.fetchall()[0][0]
    percent_international = (international_count / total_count * 100) if total_count else 0

    # 3. Average GPA, GRE, GRE V, GRE AW (where provided)
    cur.execute("SELECT AVG(gpa), AVG(gre), AVG(gre_v), AVG(gre_aw) FROM applicant WHERE gpa IS NOT NULL OR gre IS NOT NULL OR gre_v IS NOT NULL OR gre_aw IS NOT NULL;")
    avg_gpa, avg_gre, avg_gre_v, avg_gre_aw = cur.fetchall()[0]

    # 4. Average GPA of American students in Fall 2025
    cur.execute("SELECT AVG(gpa) FROM applicant WHERE us_or_international ILIKE '%American%' AND term ILIKE '%Fall 2025%' AND gpa IS NOT NULL;")
    avg_gpa_american_fall2025 = cur.fetchall()[0][0]

    # 5. Percent of Fall 2025 entries that are Acceptances
    cur.execute("SELECT COUNT(*) FROM applicant WHERE term ILIKE '%Fall 2025%' AND status ILIKE '%Accept%';")
    accept_count = cur.fetchall()[0][0]
    percent_accept = (accept_count / fall_2025_count * 100) if fall_2025_count else 0

    # 6. Average GPA of Fall 2025 Acceptances
    cur.execute("SELECT AVG(gpa) FROM applicant WHERE term ILIKE '%Fall 2025%' AND status ILIKE '%Accept%' AND gpa IS NOT NULL;")
    avg_gpa_accept_fall2025 = cur.fetchall()[0][0]

    # 7. Entries for JHU, Masters, Computer Science
    cur.execute("SELECT COUNT(*) FROM applicant WHERE program ILIKE '%Johns Hopkins%' AND degree ILIKE '%Master%' AND program ILIKE '%Computer Science%';")
    jhu_masters_cs_count = cur.fetchall()[0][0]

    cur.close()
    conn.close()

    return {
        "fall_2025_count": fall_2025_count,
        "percent_international": f"{percent_international:.2f}%",
        "avg_gpa": avg_gpa,
        "avg_gre": avg_gre,
        "avg_gre_v": avg_gre_v,
        "avg_gre_aw": avg_gre_aw,
        "avg_gpa_american_fall2025": avg_gpa_american_fall2025,
        "percent_accept": f"{percent_accept:.2f}%",
        "avg_gpa_accept_fall2025": avg_gpa_accept_fall2025,
        "jhu_masters_cs_count": jhu_masters_cs_count
    }

@app.route('/')
def index():
    results = get_query_results()
    html = '''
    <html>
    <head>
        <title>Analysis</title>
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <h1>Analysis</h1>
        <div class="qa"><span class="q">1. How many entries do you have in your database who have applied for Fall 2025?</span><br><span class="a">{{ results.fall_2025_count }}</span></div>
        <div class="qa"><span class="q">2. What percentage of entries are from international students (not American)? (to two decimal places)</span><br><span class="a">{{ results.percent_international }}</span></div>
        <div class="qa"><span class="q">3. What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?</span><br><span class="a">GPA: {{ results.avg_gpa }}, GRE: {{ results.avg_gre }}, GRE V: {{ results.avg_gre_v }}, GRE AW: {{ results.avg_gre_aw }}</span></div>
        <div class="qa"><span class="q">4. What is their average GPA of American students in Fall 2025?</span><br><span class="a">{{ results.avg_gpa_american_fall2025 }}</span></div>
        <div class="qa"><span class="q">5. What percent of entries for Fall 2025 are Acceptances (to two decimal places)?</span><br><span class="a">{{ results.percent_accept }}</span></div>
        <div class="qa"><span class="q">6. What is the average GPA of applicants who applied for Fall 2025 who are Acceptances?</span><br><span class="a">{{ results.avg_gpa_accept_fall2025 }}</span></div>
        <div class="qa"><span class="q">7. How many entries are from applicants who applied to JHU for a masters degrees in Computer Science?</span><br><span class="a">{{ results.jhu_masters_cs_count }}</span></div>
    </body>
    </html>
    '''
    return render_template_string(html, results=results)

if __name__ == '__main__':
    app.run(debug=True)
