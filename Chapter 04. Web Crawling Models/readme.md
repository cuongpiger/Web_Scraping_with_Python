# 1. Planning and Defining Objects
# 2. Dealing with Different Website Layouts
* Chương trình dưới đây sẽ tiến hành craw dữ liệu từ hai trang web dưới đây:
  * [https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html](https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html)
    ![](images/04_00.png)
  
  * [https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/](https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/)
    ![](images/04_01.png)

###### [demo_04.00.py](demo_04.00.py)
```python
import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
        
def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, "html5lib")

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find("h1").text
    lines = bs.find_all("p", {"class":"story-content"})
    body = "\n".join([lines.text for line in lines])
    
    return Content(url, title, body)

def scrapeBookings(url):
    bs = getPage(url)
    title = bs.find("h1").text
    body = bs.find("div", {"class":"post-body"}).text
    
    return Content(url, title, body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
content = scrapeNYTimes(url)
print(">> Title: {}".format(content.title))
print(">> URL: {}".format(content.url))
print(content.body)

url = "https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/"
content = scrapeBookings(url)
print(">> Title: {}".format(content.title))
print(">> URL: {}".format(content.url))
print(content.body)
```
![](images/04_02.png)