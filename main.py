#
# 爬取图片

import requests
from bs4 import BeautifulSoup

# url = "https://unsplash.com/t/wallpapers"
url = "https://www.python.org"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

# https://juejin.cn/post/7252508307646726199?searchId=20230725213010557FAEA2DD625522CDE2
#
# file=open('b.html','w')
# file.write(soup.string)
# file.close()