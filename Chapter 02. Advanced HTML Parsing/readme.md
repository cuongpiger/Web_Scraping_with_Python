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

## 2.1. `find()` and `find_all()` with BeautifulSoup
### 2.1.1. `find_all()`
```python
find_all(<tag>, <attributes>, <recursive>, <text>, <limit>, <keywords>)
```
* **`<tag>`**: có thể truyền vào đối số là `str` hoặc là `List[str]`, ví dụ:
  ```python
  find_all(['h1', 'h2', 'h3'])
  ```
    ###### [demo_02.01.py](demo_02.01.py)
    ```python
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bs = BeautifulSoup(html.read(), "html5lib")
    name_list = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    for name in name_list:
        print(name)
    ```
    ![](images/02_02.png)

* **`<attributes>`**: tham số này nhận đối số là một `Dict[str, *List[str]]`, ví dụ dưới đây có **`<tag>`** là `span` với **`attributes`** là các class **`green`** và **`red`**.
  ```python
  .find_all('span', {'class':{'green', 'red'}})
  ```

    ###### [demo_02.02.py](demo_02.02.py)
    ```python
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bs = BeautifulSoup(html.read(), "html5lib")
    name_list = bs.find_all('span', {'class':('green', 'red')})

    for name in name_list:
        print(name)
    ```
    ![](images/02_03.png)
* **`<recursive>`**: default là **`True`**, nó sẽ đào sâu vào tất cả các thẻ HTML để tìm, còn nếu là **`False`**, nó chỉ tìm trong thẻ HTML cấp cao nhất trong cây cấu trúc HTML của trang web của bạn sau đó dừng ko tìm nữa.
* **`<text>`**: nhận đối số là `str`, tìm kiếm dựa trên content của các thẻ HTML của đối số cần tìm:
  ```python
  .find_all(text="the prince")
  ```
    ###### [demo_02.03.py](demo_02.03.py)
    ```python
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bs = BeautifulSoup(html.read(), "html5lib")
    name_list = bs.find_all(text="the prince")

    print(">> len(name_list) = {}".format(len(name_list)))
    for name in name_list:
        print(name)
    ```
    ![](images/02_04.png)

* **`<limit>`**: giới hạn số thẻ cần tìm
    ###### [demo_02.04.py](demo_02.04.py)
    ```python
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bs = BeautifulSoup(html.read(), "html5lib")
    name_list = bs.find_all('span', {'class':('green', 'red')}, limit=7)

    print(">> len(name_list) = {}".format(len(name_list)))
    for name in name_list:
        print(name)
    ```
    ![](images/02_05.png)

* **`<keyword>`**: cái này ra đời ai cũng chửi, như shit vậy, khỏi tìm hiểu nhảm lắm, mấy cái trên đủ sài rồi.
