import requests
from bs4 import BeautifulSoup
import csv

URL = f"https://www.instagram.com/explore"

def save_to_file(links):
    file = open("dates.csv", mode="w")
    writer = csv.writer(file)
    for link in links:
        writer.writerow(link)
    return

def extract_links(tag):
    links = []
    result = requests.get(f"{URL}/tags/{tag}")
    soup = BeautifulSoup(result.text, "html.parser")
    links = soup.find_all("div",{"class":"Nnq7C"})
    print(links)
    return links

def get_posts(tag):
    extract_links(tag)
    return


