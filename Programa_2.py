import requests
import bs4
#import json
site = requests.get("https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)")
Lista=[]
objectSoup = bs4.BeautifulSoup(site.text,features="lxml")
site_1 = objectSoup.find(class_="mw-parser-output")
site_3 = site_1.find_all("p")    
for eachA in site_3:
    dicio = eachA.getText().capitalize().strip()
    Lista.append(dicio)
for a in Lista:
    print(a)


