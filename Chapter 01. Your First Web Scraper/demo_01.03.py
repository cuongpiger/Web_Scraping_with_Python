from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as err:
    print(err)
except URLError as err:
    print('The server could not be found!')
else:
    print('It Worked!')
    
print("Dòng này luôn chạy dù except block xảy ra")