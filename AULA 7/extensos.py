from num2words import num2words 
from os import system
system('cls')
numero = int(input('Informe um número: ')) 
print(num2words(numero, lang='pt_BR'))
