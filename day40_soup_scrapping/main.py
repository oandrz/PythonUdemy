from bs4 import BeautifulSoup
# import lxml >> parser for xml content

with open(file="./website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title) # get title
print(soup.title.string) #get string inside object
print(soup.prettify()) # to indent the html content

print(soup.a) # get first a content
print(soup.find_all(name="a")) # give all the anchor tag, output: [<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]

# To get anchor tag string
for tag in soup.find_all(name="a"):
    print(tag.getText())
    print(tag.get("href")) # get value of any attribute in this example it will strip out the link

# get based on id
heading = soup.find(name="h1", id="name")
print(heading) # output: <h1 id="name">Angela Yu</h1>

# get based on class
section_heading = soup.find(name="h3", class_="heading")
print(section_heading) # <h3 class="heading">Books and Teaching</h3>

# search a tag that sits inside p tag
company_url = soup.select_one(selector="p a") # give first match item
print(company_url) # <a href="https://www.appbrewery.co/">The App Brewery</a>

name = soup.select_one(selector="#name") # get in selector using id
print(name) # <h1 id="name">Angela Yu</h1>


headings = soup.select(".heading") # select element that has a class of theading
print(headings) # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]
