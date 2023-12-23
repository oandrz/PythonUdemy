from bs4 import BeautifulSoup
import requests

url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

response = requests.get(url)
page = response.text

soup_page = BeautifulSoup(page, "html.parser")
# print(soup_page.prettify())

with open(file="college_price.csv", mode='w') as f:
    f.write("Rank,Major,Degree Type,Early Career Pay,Mid-Career Pay,% High Meaning\n")

with open(file="college_price.csv", mode='a') as f:
    for tbody in soup_page.find_all(name="tbody"):
        rows = tbody.find_all("tr")
        for row in rows:
            # Find all the cells within the row
            cells = row.find_all("td")

            column = ""
            # Extract the data from each cell and print it
            for cell in cells:
                column += cell.get_text().split(":")[1] + ","
            f.write(column + "\n")
print("Success")

