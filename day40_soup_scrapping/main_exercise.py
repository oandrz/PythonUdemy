from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"
response = requests.get(url)
page = response.text

soup_page = BeautifulSoup(page, "html.parser")
title = [title.text for title in soup_page.select(".title .titleline")]
link = [title.get("href") for title in soup_page.select(".title .titleline > a")] # access direct child with tag a
scores = [int(score.text.split(" ")[0]) for score in soup_page.select(".subtext .subline .score")]
print(link)
print(title)
print(scores)

largest_number = max(scores)
largest_index = scores.index(largest_number)
print(largest_index)

print(f"{title[largest_index]} {link[largest_index]} {scores[largest_index]}")