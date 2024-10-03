import requests
from bs4 import BeautifulSoup

def get_urls(a_tegs):
    url_songs = []
    for link in a_tegs:
        song_path = link.get('href').split("/")[2]
        url_songs.append(song_path)

    return url_songs

def get_song_from_urls(urls):
    songs = []

    for url_song in url_songs:
        response = requests.get(URL + url_song)


        soup = BeautifulSoup(response.text, 'html.parser')

        html_song = soup.find_all("div",  {'id': 'cont'})[0]
        str_html = str(html_song.find_all("div")[1])
        if len(str_html.split("</p>")) ==4 or "Альбом:" in str_html:
            i = 2
        else:
            i = 1
                    
        line_text = str_html.split("</p>")[i].split("<p>")[0].replace("\xa0", " ").split("<br/>")
        song = " ".join(line_text).replace("  "," ").replace("  ", " ")
            
        songs.append(song)

    return songs



URL = "https://www.gr-oborona.ru/texts/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find_all("table",  {'id': 'content'})[0]
a_tegs =table.find_all("a")

url_songs  = get_urls(a_tegs)

songs = get_song_from_urls(url_songs)


with open('./data/text/songs.txt', 'w',encoding="utf-8") as file:
    for item in songs:
        file.write(item + '\n')