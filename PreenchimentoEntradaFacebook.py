import mechanicalsoup #importa a mechanicalsoup
import getpass #importa o getpass
browser = mechanicalsoup.StatefulBrowser(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',)#Passa os atributos do mechanical soup para uma variável
browser.open("https://www.facebook.com")#faz o requerimento do site
page = browser.select_form('form[id="login_form"]')#Seleciona a tag form com a atributo id="login_form"
print(page)
browser["email"] = input("Insira seu email: ")# Insere o email 
browser["pass"] = input('Insira sua senha: ')# Insere a senha

browser.launch_browser()#Lança os atributos
page = browser.get_current_page()#Pega o código html do site
print(page)
