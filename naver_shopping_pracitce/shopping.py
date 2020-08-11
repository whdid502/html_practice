import requests
from bs4 import BeautifulSoup
import json


headers = {
    'authority': 'search.shopping.naver.com',
    'accept': 'application/json, text/plain, */*',
    'urlprefix': '/api',
    'logic': 'PART',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.shopping.naver.com/search/all?frm=NVSHTTL&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=date&timestamp=&viewType=list',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=4UXIIDFH2YAV6; NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; m_loc=d00c1dd504e201ea0d12ab5c85134cc8534c2ab981a6aa06cc83582fd2913e92; nx_ssl=2; JSESSIONID=89A83C6219269614C15E618EAD614D7F; AD_SHP_BID=14; spage_uid=',
}

params = (
    ('sort', 'rel'),
    ('pagingIndex', '1'),
    ('pagingSize', '40'),
    ('viewType', 'list'),
    ('productSet', 'total'),
    ('query', '\uB178\uD2B8\uBD81'),
    ('origQuery', '\uB178\uD2B8\uBD81'),
    ('iq', ''),
    ('eq', ''),
    ('xq', ''),
    ('frm', 'NVSHTTL'),
    ('window', ''),
)

response = requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params)
result = json.loads(response.text)

with open(./)