import requests
from bs4 import BeautifulSoup


URL = "https://www.thegradcafe.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="tw-divide-y tw-divide-gray-200 tw-bg-white")

print(results)

