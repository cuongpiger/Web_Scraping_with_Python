# 1. You Don’t Always Need a Hammer
* Đôi khi việc bàn cần lấy thông tin trong một đống các thẻ HTML lồng nhau mà nếu mấy thằng gà viết sẽ như thế này:
  ```python
  bs.find_all('table')[4].find_all('tr')[2].find('td').find_all('div')[1].find('a')
  ```
  OK, đồng ý là ko sai nhưng nó xấu quá chời vs nhìn ko dc bờ-rồ cho lắm. Rồi vào một ngày đẹp trời, quản trị viên của web nơi bạn crawl dữ liệu thay đổi cấu trúc HTML của trang web thì cái mớ code trên sẽ đi bụi...

# 2. Another Serving of BeautifulSoup
* Đôi khi, ko nhất thiết ta cứ việc phải bấm vào các HTML element để crawl data, ta có thể crawl data dựa vào **class** và **id** của CSS.
* Dưới đây là trang web ví dụ cho phần này: [http://www.pythonscraping.com/pages/warandpeace.html](http://www.pythonscraping.com/pages/warandpeace.html)
  ![](images/02_00.png)

* Đoạn code dưới đây sẽ tìm kiếm mọi thẻ **`span`** mà có class là **`green`**, sau đó lấy nội dung bên trong các thẻ span đó:

###### [demo_02.00.py](demo_02.00.py)
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html5lib")
name_list = bs.findAll('span', {'class':'green'}) # tìm tất cả thẻ `span` mà có class là `green`

for name in name_list:
    print(name.get_text())
```
![](images/02_01.png)