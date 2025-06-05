# GradCafe Data Analysis Project

## Overview
This project imports graduate application data from a JSON file into a PostgreSQL database, analyzes the data with SQL queries, generates a PDF report, and displays the results on a Flask web page.

## Project Structure
```
module_3/
├── load_data.py              # Script to load JSON data into PostgreSQL
├── query_data.py             # Script to run analysis queries and generate PDF report
├── requirements.txt          # Python dependencies (pip freeze format)
├── grad-analysis-page/
│   ├── app.py                # Flask web app to display analysis results
│   └── static/
│       └── style.css         # CSS for Flask app
├── query_results.pdf         # Generated PDF report (after running query_data.py)
```

## Setup Instructions
1. **Install Python dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Set up PostgreSQL**
   - Create a database named `GradCafe`.
   - You do not need to manually create the `applicant` table. The table and its column descriptions will be created automatically when you run `load_data.py`.
3. **Import Data**
   - The JSON data file `application_data.json` is already included in this folder by default. No path changes are needed.
   - Run:
     ```powershell
     python load_data.py
     ```
4. **Run Analysis and Generate PDF**
   ```powershell
   python query_data.py
   ```
   This will create `query_results.pdf` with the analysis results.
5. **Run the Flask Web App**
   - From the `module_3` directory, run:
     ```powershell
     python grad-analysis-page/app.py
     ```
   - Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Notes
- The Flask app displays the same analysis as the PDF report.
- Make sure your PostgreSQL server is running and accessible.
- The requirements.txt is in pip freeze format for easy environment replication.

---

This README was generated with the help of GitHub Copilot.

