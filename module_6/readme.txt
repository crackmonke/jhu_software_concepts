# GradCafe Scraper

This project scrapes graduate school application results from TheGradCafe, cleans the data, and saves it to a JSON file.

## Files

- `scrape.py`: Scrapes application data from TheGradCafe.
- `clean.py`: Cleans and processes the scraped data.
- `robot.py`: Checks if scraping is allowed by the site's robots.txt.
- `requirements.txt`: Lists required Python packages.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the scraper:
   ```
   python scrape.py
   ```

## Notes

- By default, the scraper fetches up to 1000 pages of results.  
- **To change the number of pages scraped:**  
  Open `scrape.py` and modify the value passed to `scrape_data(max_pages=...)` in the `if __name__ == "__main__":` block at the bottom of the file.  
  For example, to scrape 5 pages, change it to `scrape_data(max_pages=5)`.
- Cleaned data is saved as `application_data.json`.

## Requirements

- Python 3.x
- See `requirements.txt` for package versions.

1. Name: Savannah Greeley, 26CF07

2. Module Info:
   - Module: Module 2 – Web Scraping
   - Assignment: Module 2 - Assignment: Web Scraping
   - Due Date: June 2nd 11:59 PM EST

3. Approach:
   For this assignment, I created a Python project to scrape graduate school application results from TheGradCafe website. My approach included the following steps:

   - **robots.txt Check:** I implemented a `robot.py` script to check the site's robots.txt file and ensure scraping is permitted.
   - **Scraping:** The `scrape.py` script uses the `requests` and `BeautifulSoup` libraries to fetch and parse HTML pages from TheGradCafe. It iterates through up to 10 pages (by default) and extracts relevant application data (such as school, program, decision, and date) into a list of dictionaries.
   - **Data Cleaning:** The `clean.py` script processes the raw scraped data, standardizing field names, removing duplicates, and handling missing or malformed entries. The cleaned data is then saved as `application_data.json`.
   - **Dependencies:** All required packages are listed in `requirements.txt` for easy installation.

   I structured the code to separate scraping, cleaning, and robots.txt checking for modularity and easier debugging.

4. Known Bugs:
   - As of submission, there are no known bugs. If any issues are discovered (such as missing fields or failed requests), I would add error handling (try/except blocks) and logging to identify and fix the problem.

## Acknowledgements

This README was created with the assistance of GitHub Copilot, an AI programming assistant.
