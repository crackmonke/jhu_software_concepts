Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> from urllib.request import urlopen
>>> 
>>> url = "http://olympus.realpython.org/profiles/dionysus"
>>> page = urlopen(url)
>>> html = page.read().decode("utf-8")
>>> 
>>> pattern = "<title.*?>.*?</title.*?>"
>>> match_results = re.search(pattern, html, re.IGNORECASE)
>>> title = match_results.group()
>>> title = re.sub("<.*?>", "", title) # Remove HTML tags
>>> 
>>> print(title)
Profile: Dionysus
