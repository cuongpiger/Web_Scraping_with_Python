from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url: str) -> str:
    try:
        html = urlopen(url)
    except HTTPError as err:
        return None
    
    try:
        bs = BeautifulSoup(html.read(), 'html5lib')
        title = bs.body.h1
        
    except AttributeError as err:
        return None
    
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Không có title')
else:
    print(title)