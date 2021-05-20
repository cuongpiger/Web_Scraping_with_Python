from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser') 
print(bs.h1)

# 3 lệnh này tương ứng vs lệnh trên
print(bs.html.body.h1)
print(bs.body.h1)
print(bs.html.h1)