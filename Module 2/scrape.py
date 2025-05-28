import requests
from bs4 import BeautifulSoup


URL = "https://www.thegradcafe.com/survey/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("table", class_="tw-min-w-full tw-divide-y tw-divide-gray-300")

for result in results:  
    data_rows = result.find_all("tr")
    for data_row in data_rows:
        university_name_tag = data_row.find("div", class_="tw-font-medium tw-text-gray-900 tw-text-sm")
        if university_name_tag:
            university_name = university_name_tag.get_text(strip=True)
            print(university_name)

# program_name
# university_name
# comments (if available)
# date_added
#url_to_applicant_entry
# application_status
##if accepted, then acceptance_date
##if rejected, then rejection_date
#Semester and year of program start (if available)
#international_or_american_student (if available)
#GRE_score (if available)
#GRE_V_score (if available)
#Master's_or_PhD (if available)
# GPA (if available)
# GRE_AW_score (if available)

