# 1. Connecting
* Trang web [http://pythonscraping.com/pages/page1.html](http://pythonscraping.com/pages/page1.html)
  ![](images/01_00.png)

* Code dưới đây sẽ lấy toàn bộ mã HTML của trang web trên.
###### [demo_01.00.py](demo_01.00.py)
```python
from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
```
![](images/01_01.png)

# 2. An Introduction to BeautifulSoup
* Thư viện này dùng để xử lí các mã HTML khi crawl dữ liệu từ web về.
  
## 2.1. Installing BeautifulSoup
* Mở terminal và chạy lệnh `pip3 install beautifulsoup4`.
  ![](images/01_02.png)

## 2.2. Running BeautifulSoup
* Đoạn code dưới đây trả về thẻ **`h1`** đầu tiên được tìm thấy trên trang cùng với content bên trong thẻ này.
* Dòng code dưới đây chuyển `html` thành object BeautifulSoup:
  ```python
  bs = BeautifulSoup(html, 'html.parser')
  ```
  từ đây có thể truy cập vào các HTML element bằng các cách dưới đây:
  ![](images/01_04.png)
* Dưới đây là toàn bộ mã nguồn:
###### [demo_01.01.py](demo_01.01.py)
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser') 
print(bs.h1)

# 3 lệnh này tương ứng vs lệnh trên
print(bs.html.body.h1)
print(bs.body.h1)
print(bs.html.h1)
```
![](images/01_03.png)