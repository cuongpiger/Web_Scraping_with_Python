from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html5lib")
name_list = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

for name in name_list:
    print(name)