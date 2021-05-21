from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html5lib")
name_list = bs.find_all('span', {'class':('green', 'red')})

for name in name_list:
    print(name)