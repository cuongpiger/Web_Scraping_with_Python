from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
tags = bs.find_all(lambda tag: len(tag.attrs) == 2)

for tag in tags:
    print("=>> {}".format(tag))