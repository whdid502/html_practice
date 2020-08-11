import requests
from bs4 import BeautifulSoup


URL = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie_li = soup.select('div.lst_wrap > ul.lst_detail_t1 > li')
movie_code_li = []
# print(movie_li)
for i in movie_li:
    movie_title = i.select_one('dt.tit > a').text
    movie_href =  i.select_one('dt.tit > a')['href']
    movie_code = movie_href.split('=')[1]
    movie_dic = {'movie' : movie_title, 'code' : movie_code}
    movie_code_li.append(movie_dic)

for i in movie_code_li:
    headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189069&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=sympathyScore&page=2',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=4UXIIDFH2YAV6; NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; m_loc=d00c1dd504e201ea0d12ab5c85134cc8534c2ab981a6aa06cc83582fd2913e92; nx_ssl=2; JSESSIONID=651C01216CE110EE35ED3B90F24F74C1; csrf_token=7517932f-7894-4a72-9862-2106e6e4716f; NM_VIEWMODE_AUTO=basic',
    }

    params = (
        ('code', movie_code_li['code']),
        ('type', 'after'),
        ('onlyActualPointYn', 'N'),
        ('onlySpoilerPointYn', 'Y'),
        ('order', 'sympathyScore'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')

    review_list = soup.select('body > div > div > div.score_result > ul > li')

    count = 0
    for j in review_list:
        score = ''
        reple = ''
        score = j.select_one('div.star_score > em').text
        reple = j.select_one('div ')