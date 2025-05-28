import requests
from bs4 import BeautifulSoup


URL = "https://www.thegradcafe.com/survey/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("tbody", class_="tw-divide-y tw-divide-gray-200 tw-bg-white")

print(results)

for result in results:  
    data_rows = result.find("div", class_="tw-divide-y tw-divide-gray-200 tw-bg-white")
    if data_rows:
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
        pass