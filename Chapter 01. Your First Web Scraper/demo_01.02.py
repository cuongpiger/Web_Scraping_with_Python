from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as err:
    print(err)
else:
    print("Else block này sẽ chạy nếu except block ko xảy ra")

print("Sẽ luôn print dòng này dù except block hay else block xảy ra")