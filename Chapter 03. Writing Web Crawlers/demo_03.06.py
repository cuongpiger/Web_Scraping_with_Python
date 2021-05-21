from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Trả về tất cả các đường dẫn hiện có trên một trang cụ thể
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    """
    .scheme: trả về `str` cho biết là http hay https
    .netloc: trả về địa chỉ thuẩn chủng của trang, ví dụ facebook.com/cuongpiger thì chỉ trả về facebook.com thôi
    """
    internalLinks = []
    # tìm tất cả các đường dẫn bắt đầu với "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    
    return internalLinks

# Truy xuất đến tất cả các liên kết ngoài trên 1 trang cụ thể
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # tìm kiếm tất cả các URL bắt đầu bằng http mà ko chứa url hiện tại
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    
    return externalLinks

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
            
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)
    
allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')