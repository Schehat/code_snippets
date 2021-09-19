import os
from bs4 import BeautifulSoup

os.chdir(os.path.dirname(__file__))

with open("simple.html", encoding="UTF-8") as html_file:
    soup = BeautifulSoup(html_file, "lxml")  # input: the html file & parser: lxml

# print(soup.prettify())  # print whole html, prettify just intends the blocks

# by accessing it like an attribute only the first hit will be returned
print(f"title with tags: {soup.title}")

print(f"title without tags: {soup.title.text}\n")

# find without further argument equals soup.div and returns first hit
print(f"get first div:\n{soup.find('div')}\n")

print(f"get div with footer class:\n{soup.find('div', class_='footer')}\n")

article = soup.find("div", class_="article")
print(f"article:\n{article}\n")

# article can be further inspected like soup
print(f"headline of article: {article.h2.a.text}")
print(f"summary of article: {article.p.text}")

print("\nget every article\n")

for article in soup.find_all("div", class_="article"):
    # article can be further inspected like soup
    print(f"headline of article: {article.h2.a.text}")
    print(f"summary of article: {article.p.text}\n")
