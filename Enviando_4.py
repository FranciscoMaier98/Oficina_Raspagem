import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
site = browser.open("https://www.facebook.com/?stype=lo&jlou=AfeAYAtmUKQJXrrS0Xfo86y_m1MqmiXWIXvRAHyJB2hz1DIoHqmCzcHWCZhCHQyfUQ8J4bAHa3eFIDXmTo1N_yG-G9kJxYP9U9KTmQxzEJMvxw&smuh=53600&lh=Ac9O4IFGFaAv2FQd")
print(site)

hue1=browser.get_current_page()
hue2=browser.get_current_page().find_all('form')#Dentro da pagina encontra todas as tags legend
hue3=browser.select_form('form[method="post"]')#seleciona a tag do programa

browser.get_current_form().print_summary()#Aqui ele printa todos os inputs

#Aqui ele escreve em cada um dos tópicos
browser['email'] = "chicosm@outlook.com"
browser['pass'] = "Soundwave98"

browser.launch_browser()#Lança todos os dados para o site
