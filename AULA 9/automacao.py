from requests import get
from bs4 import BeautifulSoup
from os import system
system('cls')

url = "https://economia.uol.com.br/"
response = get(url)#aqui o requests lê a pagina e trás o html
html_soup = BeautifulSoup(response.text, "html.parser")
print(html_soup)
#print(html_soup)
#cotacao = html_soup.find_all('span', class_ = 'value bra')
cotacao= html_soup.find_all('a', class_ ='subtituloGrafico subtituloGraficoValor')
print(len(cotacao))
print(cotacao)
for valor in cotacao:
    print(valor.text)
