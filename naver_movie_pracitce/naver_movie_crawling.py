import requests
from bs4 import BeautifulSoup


base_url = 'https://movie.naver.com/movie/running/current.nhn'
start_num = str(i)
end_url = '&refresh_start=0'

URL = base_url + start_num + end_url

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')