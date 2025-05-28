import requests
from bs4 import BeautifulSoup


URL = "https://www.thegradcafe.com/survey/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("div", class_="tw-gap-2 tw-flex tw-flex-wrap")


for result in results:  
    application_status = result.find("div", class_="tw-inline-flex tw-items-center tw-rounded-md tw-bg-sky-50 tw-text-sky-700 tw-ring-sky-600/20 tw-px-2 tw-py-1 tw-text-xs tw-font-medium tw-ring-1 tw-ring-inset md:tw-hidden")
    if application_status:
        print(application_status.get_text(strip=True))
    else:
        print("No application status found")

