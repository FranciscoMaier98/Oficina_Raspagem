import mechanicalsoup
import getpass
browser = mechanicalsoup.StatefulBrowser(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',)
browser.open("https://www.facebook.com")
print(browser.get_url())
browser.select_form('form[id="login_form"]')
#browser.get_current_form().print_summary()
browser["email"] = input("Insira seu email: ")
browser["pass"] = getpass.getpass('Insira sua senha: ')
#browser["TIPO_USU"] = "1"
#browser.launch_browser()
response = browser.submit_selected()
#print(response.text)
page = browser.get_current_page()
#print(browser.get_url())
print(page)
