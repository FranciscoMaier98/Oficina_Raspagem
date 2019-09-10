import requests #importa a biblioteca reqests
import bs4 #importa a biblioteca bs4

Lista=[]

url = 'https://www.vagalume.com.br/top100/musicas/'
html = requests.get(url)#Requisição do site

sopa = bs4.BeautifulSoup(html.text, 'html.parser') #pega o código de html
musicas = sopa.find_all(class_="w1 h22") #Busca a parte do código com o atributo class_="w1 h22"

#Com filtro
for m in musicas:
    print(m.get_text().capitalize().strip().replace('(traduã§ã£o)','')) #Filtrando o texto e printando na tela



