from bs4 import BeautifulSoup
import requests

url =  requests.get('http://www.climatempo.com.br/').content

soup = BeautifulSoup(url, 'html.parser')

temperatura = soup.find("img", class_="_margin-l-10 _margin-r-5")

print(temperatura.string)
