Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.findall("ab*c", "ac")
['ac']
>>> re.findall("ab*c", "abcd")
['abc']
>>> re.findall("ab*c", "acc")
['ac']
>>> re.findall("ab*c", "ABC")
[]
>>> re.findall("ab*c", "ABC", re.INGORECASE)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    re.findall("ab*c", "ABC", re.INGORECASE)
AttributeError: module 're' has no attribute 'INGORECASE'. Did you mean: 'IGNORECASE'?
>>> re.findall("ab*c", "ABC", re.IGNORECASE)
['ABC']

>>> re.findall("a.c", "abc")
['abc']
>>> re.findall("a.c", "acc")
... 
['acc']
