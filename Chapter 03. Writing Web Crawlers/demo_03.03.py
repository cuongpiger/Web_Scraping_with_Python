from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                pages.add(newPage)
                
                print(newPage)
                getLinks(newPage)
    
getLinks('')