import requests
import bs4
import mechanicalsoup
import re
#declarando as listas
Latitude = []
Longitude = [] 


browser = mechanicalsoup.StatefulBrowser(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',)
maps = browser.open("https://www.google.com.br/maps")
browser.get_url()
browser.get_current_page()

#Aqui Tô tentando buscar, mas sempre dá erro de n achar
browser.get_current_page().find_all('form')
browser.select_form('form[id="searchbox_form"]')#n tá achando
#já chamei outras tags, como algumas div com outros atributos, não deu certo

#parte da API, aqui funciona q é uma beleza
site = requests.get("http://api.open-notify.org/iss-now.json")
objectSoup = bs4.BeautifulSoup(site.text,features="lxml").getText()

c1 = 0

#faz a seleção só do que precisa, as cordenadas
for a in objectSoup:    
    if  c1<39 and c1>28:
        if a == '.':
            Latitude.append(a)
        elif a=='-':
            Latitude.append(a)
        else: 
            Latitude.append(re.sub('[^0-9]', '', a))
        
    elif c1>53 and c1<64:
        if a == '.':
            Longitude.append(a)
        elif a=='-':
            Longitude.append(a)
        else: 
            Longitude.append(re.sub('[^0-9]', '', a))#só pega os números
    c1+=1

#Transforma em strigns
Latitude1=''.join(Latitude) #Junta as listas
Longitude1=''.join(Longitude)#Junta as listas

#concatena as duas cordenadas com uma vírgula
junto = Latitude1 + "," + Longitude1
print(junto)

#Aqui deveria mandar!!
browser["q"] = junto

browser.submit_selected()




