import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
page = requests.get(url=URL).text
soup_page = BeautifulSoup(page, "html.parser")
result = [title.text for title in soup_page.select(".article-title-description .article-title-description__text .title")]
# another approach
all_movies = soup_page.find_all(name="h3", class_="title")
print(result)
with open("./movies.txt", mode="w") as file:
    for title in result[::-1]:
        file.writelines(f"{title}\n")

