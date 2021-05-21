from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html5lib")
name_list = bs.find_all(text="the prince")

print(">> len(name_list) = {}".format(len(name_list)))
for name in name_list:
    print(name)
