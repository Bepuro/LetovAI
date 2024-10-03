import requests
from bs4 import BeautifulSoup
import re


def clean_text(txt):
    res = str(txt)
    res = res.replace("\n"," ").replace("   "," ").replace("  "," ")
    res = re.sub(r'<[^>]+>', '', res)
    return res


URL = "https://www.gr-oborona.ru/pub/rock/egor_letov_stihi.html"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

html_poems = soup.find_all("pre")

poems = [clean_text(p) for p in html_poems]
print(poems)

with open('./data/text/poems.txt', 'w',encoding="utf-8") as file:
    for item in poems:
        file.write(item + '\n')



