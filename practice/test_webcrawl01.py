# 웹 크롤링 -> 다음 뉴스

import requests
from bs4 import BeautifulSoup
url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)

# print(result)
doc = BeautifulSoup(result.text, 'html.parser')
title = doc.select('h3.tit_view')
title2 = doc.select('h3.tit_view')[0]
title3 = doc.select('h3.tit_view')[0].get_text()

print(title)
print(title2)
print('# 뉴스 제목 : {]'.format(title3))