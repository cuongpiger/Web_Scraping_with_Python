from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html5lib")
name_list = bs.findAll('span', {'class':'green'}) # tìm tất cả thẻ `span` mà có class là `green`

for name in name_list:
    print(name.get_text())