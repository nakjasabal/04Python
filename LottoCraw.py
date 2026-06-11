import requests
from bs4 import BeautifulSoup

url = 'https://www.dhlottery.co.kr/lt645/result'
response = requests.get(url)

if response.status_code==200:  
  html = response.text  
  soup = BeautifulSoup(html, 'html.parser')
  # print(soup)
  
  title1_1 = soup.select_one('#containerBox > div.content-tit-wrap > div > h2')
  print("추출1:", title1_1)
  
else:
  print("응답없음")



 
  
  