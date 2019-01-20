from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://soundcloud.com/peggygou'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each song
containers = page_soup.findAll("article",{"class":"audible"})

filename = "peggy_gou_tunes.csv"
f = open(filename, "w")

headers = "Tune\n"

f.write(headers)

for container in containers:
    song = container.a.text

    f.write(song.replace(",", "|") + "\n")

f.close()