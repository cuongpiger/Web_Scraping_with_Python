from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
image = bs.find('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})

for att in image.attrs:
    print("{} = {}".format(att, image[att]))