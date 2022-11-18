from requests import get
from bs4 import BeautifulSoup
from os import system
system('cls')

url = "https://economia.uol.com.br/"
response = get(url)#aqui o requests lê a pagina e trás o html

