# Louie Chapman
#
# This file contains webscraping functions to make the main file more readable 


from bs4 import BeautifulSoup
import requests
from csv import writer

print("starting")

url="https://www.national.co.uk/tyres-search?width=205&profile=55&diameter=16&pc=S118FQ"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find_all("div", class_="tyreresult")

with open("data.csv", "w", encoding="utf8", newline="") as f:
    thewriter = writer(f)
    header = ["Type", "Is", "A", "Temporary", "Title"]

    
    thewriter.writerow(header)
    for list in lists:
        title = list.find("a", class_="pattern_link").text.replace("\n","")

        info = [title]
        thewriter.writerow(info)

print(len(lists))

print("finished")