import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo&year=2020&type=batter&playerOrder=hra"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

ph_rank = soup.find("ol", attrs={"class":"ph_rank"})
for index, ph in enumerate(ph_rank):
    rank = ph_rank.find_all("span", attrs={"class":"ord"})[index].get_text()
    name = ph_rank.find_all("strong")[index].get_text()
    team = ph_rank.find_all("span", attrs={"class":"team"})[index].get_text()
    win = ph_rank.find_all("em")[index].get_text()

    print(rank, name, team, win)

    if index >= 4:
        break