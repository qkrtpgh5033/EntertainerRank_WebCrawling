import requests
from bs4 import BeautifulSoup
import re
url = 'https://entertain.daum.net/ranking/popular'
html = requests.get(url).text
# print(html)
html = BeautifulSoup(html, 'html.parser')

Populars = html.find_all('strong', {'class': 'tit_thumb'})

num = 1  # 순위용 카운터

for popular in Populars:
    # print(popular)
    if popular.a == None:
        continue
    title = popular.text
    main_url = popular.a["href"] # 데이터가 없는 경우 다음으로 넘어가기


    main_html = requests.get(main_url).text
    main_html = BeautifulSoup(main_html, 'html.parser')
    main_text = main_html.find(class_="article_view").getText().strip()

    file_title = str(num) + '.txt'
    memo_file = open(file_title, 'w', encoding='utf-8')
    memo_file.write("제목 : " + title + "\n")
    memo_file.write(main_text)
    memo_file.close()
    num+=1

