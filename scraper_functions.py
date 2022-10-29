# Louie Chapman
#
# This file contains webscraping functions to make the main file more readable 


from bs4 import BeautifulSoup
import requests
from csv import writer

url="https://www.national.co.uk/tyres-search?width=205&profile=55&diameter=16&pc=S118FQ"
page = requests.get(url)

# access the webpage and download the .html
soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find_all("div", class_="tyreresult")

with open("data.csv", "w", encoding="utf8", newline="") as f:
    thewriter = writer(f)
    header = ["Source", "Brand", "Pattern", "Size", "Seasonality", "Price"]

    
    thewriter.writerow(header)
    website="www.national.co.uk"
    for list in lists:  # todo: change these variable names
        brand   = list.find("img", loading="lazy").get("alt")
        title   = list.find("a", class_="pattern_link").text.replace("\n","")
        size    = list.find("div", class_="details").find_all("p")[1].text.replace("\n","").strip()
        price   = list.find("span", class_="red text-24").text.replace("\n","").strip()

        fitment_data = list.find_all("img", class_="fitment") or {} # all fitment data , will be filtered through to find seasonality
        seasonality = ""  # seasonality output after filtering out other fitment factors ( such as brand or width )
        for data in fitment_data:
            fitment_title=data.get("title")
            if fitment_title == "All Season Tyres" or fitment_title == "Winter Tyres":
                seasonality = fitment_title
                break

        info = [website,brand,title,size,seasonality,price]  # final output
        thewriter.writerow(info)    
        # add to the table
        # eventually I'd like to save all the data into a single list and add it all at once
        # but maybe I won't do that just yet :/

print("datapoints scraped: {}".format(len(lists)))