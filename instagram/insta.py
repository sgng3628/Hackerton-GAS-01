from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas,numpy

hashtag ="food"
URL = "https://www.instagram.com"

browser = webdriver.Chrome('path/to/chromedriver')
browser.get(f"{URL}explore/tags/{hashtag}")
Pagelength = browser.execute_script("window.scrollTo(0,document.body.scrollHeight);"

links = []
source = browser.page_source
data = BeautifulSoup(source, "html.parser")
body = data.find('body')
script = body.find('script', text=lambda t:t.startswith('window._sharedData'))
page_json = script.text.split(' = ', 1)[1].rstrip(;)
data = json.loads(page_json)

for link in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
    links.append(f"{URL}/p/{link['node']['shortcode']}/")