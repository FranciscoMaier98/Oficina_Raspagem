import requests #Iniciando requests / Ela faz o pedido para o site
import bs4
from bs4 import BeautifulSoup #iniciando a BeautifulSoup / Biblioteca que manipula os dados
import json #iniciando json
from operator import itemgetter

Lista_livro=[]
Dicio_livros={}
teste=()
variavel_livros=1

livro_1 = requests.get("https://www.amazon.com.br/b?ie=UTF8&node=16271670011") #iniciando as variaveis com o mechanicalsoup
livro_2 = requests.get("https://www.livrariacultura.com.br/maisvendidos")
livro_4 = requests.get("https://veja.abril.com.br/livros-mais-vendidos/")
livro_8 = requests.get("https://www.publishnews.com.br/ranking")


try:
    

    objectSoup = bs4.BeautifulSoup(livro_1.text,features="lxml")#importa os dados do site
    listLivros_1 = objectSoup.select(class_="a-size-medium s-inline s-access-title a-text-normal")#procura a class
    for eachA in listLivros_1:
        dicio = eachA.getText().capitalize()
        Lista_livro.append(dicio)

    objectSoup = bs4.BeautifulSoup(livro_2.text,features="lxml")
    listLivros_2 = objectSoup.find_all(class_="product-font-new product-title-new")
    for eachA in listLivros_2:
        dicio = eachA.getText().capitalize()
        Lista_livro.append(dicio)



    objectSoup = bs4.BeautifulSoup(livro_4.text,features="lxml")
    listLivros_4 = objectSoup.find_all(class_="titulo")
    for eachA in listLivros_4:
        dicio = eachA.getText().capitalize()
        Lista_livro.append(dicio)


    objectSoup = bs4.BeautifulSoup(livro_8.text,features="lxml")
    listLivros_8 = objectSoup.find_all(class_="pn-ranking-livro-nome")
    for eachA in listLivros_8:
        dicio = eachA.getText().capitalize().strip()
        Lista_livro.append(dicio)
    
    for a in Lista_livro:
        valor=Lista_livro.count(a)
        if a not in Dicio_livros:
            Dicio_livros[a]=int(valor)

    teste=sorted(Dicio_livros.items(),key=itemgetter(1),reverse=True)
    
    for chave,valor in enumerate(teste):
        print(f'{chave+1} - {valor[0]}')
        variavel_livros=variavel_livros+1
        if variavel_livros==11:
            break       


    
    
except Exception as exc:
    print(exc)
