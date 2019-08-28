from bs4 import BeautifulSoup
import requests
page = requests.get('https://www.myip.com/')
soup = BeautifulSoup(page.text, 'html.parser')
soup = soup.find('span', id="ip").get_text()
print(soup)
