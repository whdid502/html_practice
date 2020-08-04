import requests
from bs4 import BeautifulSoup


URL = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie_li = soup.select('div.lst_wrap > ul.lst_detail_t1 > li')
movie_dic = {}
# print(movie_li)
for i in movie_li:
    movie_title = i.select_one('dt.tit > a').text
    movie_href =  i.select_one('dt.tit > a')['href']
    movie_code = movie_href.split('=')[1]

    movie_dic[movie_title] = movie_code

print(movie_dic)