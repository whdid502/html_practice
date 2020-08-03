import requests
from bs4 import BeautifulSoup
import csv

soup_obj = []

f = open('./news.csv', 'wt', encoding='utf-8', newline="")
writer = csv.writer(f)

for i in range(1,102,10):

    base_url = 'https://search.naver.com/search.naver?&where=news&query=광주인공지능사관학교&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
    start_num = str(i)
    end_url = '&refresh_start=0'

    URL = base_url + start_num + end_url

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    soup_obj.append(soup)
    # print(soup_obj)

for i in soup_obj:

    news_section = i.select('div#main_pack > div.news.mynews.section._prs_nws > ul.type01 > li')

    for news in news_section:
        news_a_tag = news.select_one('dl > dt > a')
        news_link = news_a_tag['href']
        news_title = news_a_tag['title']
        news_dir = {
            'title' : news_title,
            'link' : news_link
        }
        writer.writerow([news_title, news_link])
        # print(news_dir)

f.close()