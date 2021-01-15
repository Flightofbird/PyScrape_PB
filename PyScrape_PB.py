from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
import datetime

print("Scrivi l'indirizzo eg: Via Savoniero         Also type &p=2 for page 2")
ats = input()
my_url = ("https://www.paginebianche.it/cerca-da-indirizzo?dv=Modena+" + ats.replace(" ", "+" ))
#my_url = "https://www.paginebianche.it/cerca-da-indirizzo?dv=Modena+Via+Savoniero"

#grab date
Current_Date = datetime.datetime.today().strftime ('%d-%m-%Y')

#Read url from text
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = bs(page_html, "html.parser")

item = page_soup.findAll("div",{"class":"item"})
bigtitle = page_soup.findAll("h1",{"class":"listing-h1"})
bigtitle_fin = bigtitle[0].find("strong").text[15:]

#writing the CSV
filname = (bigtitle_fin + "_da_paginebianche_" + Current_Date + ".csv")
f = open(filname, "w")

headers = "Nome, Indirizzo, Tele\n"

f.write(headers)

#finding the text
for container in item:
    title = container.div.a["title"]

    address = container.findAll("span", {"class":"street-address"})
    final_address = address[0].text

    postcode = container.find("span", itemprop="postalCode")
    final_pc = postcode.text

    city = container.find("span", itemprop="addressLocality")
    final_city = city.text

    tele = container.find("span", itemprop="telephone")
    final_tele = tele.text

    adDress = (final_address + " - " + final_pc + " " + final_city)

    f.write(title + "," + adDress.replace(",", "-") + "," + final_tele.replace(" ", "/") + "\n")
f.close()
print("Success!")
