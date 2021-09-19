import os
import csv
from bs4 import BeautifulSoup
import requests

os.chdir(os.path.dirname(__file__))

# get source code of a website
# get-method returns respond object, to get source code add .text
source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, "lxml")

with open("cms_scraper.csv", "w", encoding="UTF-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["headline", "summary", "video_link"])

    for article in soup.find_all("article"):
        headline = article.h2.a.text
        print(headline)

        summary = article.find("div", class_="entry-content").p.text
        print(summary)

        # prevent rnt error when an article doesent have a youtube video
        try:
            # can access like a dict
            vid_src = article.find("iframe", class_="youtube-player")["src"]
            vid_id = vid_src.split("/")[4]
            vid_id = vid_id.split("?")[0]

            yt_link = f"https://youtube.com/watch?v={vid_id}"
        except TypeError:
            yt_link = None

        print(f"{yt_link}\n")

        csv_writer.writerow([headline, summary, yt_link])
