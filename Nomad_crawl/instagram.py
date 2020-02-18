import requests
from bs4 import BeautifulSoup
import csv

URL = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"

def extract_links():
    datas = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    page = soup.find("div",{"id":"ranking_101"})
    results = page.find_all("li")
    for result in results:
        temp = result.find("a")
        print(temp)
        num = result.find("span").get_text()
        print(num)
        link = URL+temp.get("href")
        print(link)
        title = temp["title"]
        print(title)
    return 

def get_posts():
    extract_links()
    return


