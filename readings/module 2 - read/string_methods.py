Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from urllib.request import urlopen
>>> url = "http://olympus.realpython.org/profiles/aphrodite"
>>> page = urlopen(url)
>>> page
<http.client.HTTPResponse object at 0x0000020623534970>
>>> html_bytes = page.read()
>>> html = hml_bytes.decode("utf-8")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    html = hml_bytes.decode("utf-8")
NameError: name 'hml_bytes' is not defined. Did you mean: 'html_bytes'?
>>> 
>>> html = html_bytes.decode("utf-8")
>>> print(html)
<html>
<head>
<title>Profile: Aphrodite</title>
</head>
<body bgcolor="yellow">
<center>
<br><br>
<img src="/static/aphrodite.gif" />
<h2>Name: Aphrodite</h2>
<br><br>
Favorite animal: Dove
<br><br>
Favorite color: Red
<br><br>
Hometown: Mount Olympus
</center>
</body>
</html>

>>> title_index = html.find("<title>")
>>> title_index
14
>>> start_index = title_index + len("<title>")
>>> start_index
21
>>> end_index = html.find("</title>")
>>> end_index
39
title = html[start_index:end_index]
titlle
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    titlle
NameError: name 'titlle' is not defined. Did you mean: 'title'?
title
'Profile: Aphrodite'
