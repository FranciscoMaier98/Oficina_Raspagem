import requests #importa a biblioteca reqests
import bs4 #importa a biblioteca bs4

Lista=[]

url = 'https://www.vagalume.com.br/top100/musicas/'
browser = requests.get(url)#Requisição do site

html = bs4.BeautifulSoup(browser.text, 'html.parser') #pega o código de html
musicas = html.find_all(class_="w1 h22") #Busca a parte do código com o atributo class_="w1 h22"

#Com filtro
for m in musicas:
    print(m.get_text().capitalize().strip().replace('(traduã§ã£o)','')) #Filtrando o texto e printando na tela



