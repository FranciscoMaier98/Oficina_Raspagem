from bs4 import BeautifulSoup #Chama a biblioteca bs4
import requests #Chama a biblioteca requests
page=requests.get('https://www.myip.com/')#FAz a requisição do site
soup = BeautifulSoup(page.text, 'html.parser')#Pega o código html do site
soup = soup.find('span', id="ip").get_text()#Encontra a tag span com o atributo id="pi"
print(soup)#printa o valor encontrado
