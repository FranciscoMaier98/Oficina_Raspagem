import bs4 
import requests

Lista = []

site = requests.get("https://oglobo.globo.com/brasil/pf-se-manifesta-pela-soltura-de-amigos-de-hacker-preso-23918343")
objectSoup = bs4.BeautifulSoup(site.text,features="lxml")

site_titulo_1 = objectSoup.find('h1',class_="article__title").get_text()
print("TÍTULO")
print(site_titulo_1)

print("TEXTO")
print("")
site_texto_1 = objectSoup.find(class_="article__content-container protected-content")
site_texto_2 = site_texto_1.find_all("p")

for a in site_texto_2:
    dicio = a.getText().strip()
    Lista.append(dicio)

for a in range(0,8,1):
   
   if a==1:
       continue
   print(Lista[a])
   
