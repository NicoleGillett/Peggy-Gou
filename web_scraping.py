import requests
from bs4 import BeautifulSoup

my_url = 'https://soundcloud.com/peggygou'

# request the page
page = requests.get(my_url)

# html parsing
page_soup = BeautifulSoup(page.text, "html.parser")

# grab each song
containers = page_soup.findAll("article",{"class":"audible"})

filename = "peggy_gou_tunes.csv"

with open(filename, "w") as f:

    headers = "Tune\n"

    f.write(headers)

    for container in containers:
        song = container.a.text

        f.write(song.replace(",", "|") + "\n")