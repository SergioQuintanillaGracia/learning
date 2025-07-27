import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(selector=".article-title-description__text .title")
titles = [title.text for title in titles]
titles.reverse()

with open("movies.txt", "a") as f:
    for title in titles:
        f.write(f"{title}\n")