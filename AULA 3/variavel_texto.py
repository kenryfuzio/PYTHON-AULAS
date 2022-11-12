from os import system #importa as bibliotecas do sistema operacional
system('cls')
#criação de variável texto 
#as variaveis devem seguir um padrão
#snake_case, Pascalcase ou camelCase
#nome_completo
#NomeCompleto
#nomeCompleto
nome_completo= "Kenry Edwin Fuzio Silva"
print(len(nome_completo)) #len= conta a quantidade de caracteres
print(nome_completo.count('e'))#conta a repetição de um caracter    
print(nome_completo.upper())#deixa todas as letras maiusculas
print(nome_completo.lower())#deixa todas as letras minusculas
print(nome_completo.capitalize())#deixa apenas a primeira letra maiuscula
print(nome_completo.find(' ')) #serve para achar caracter
espaco = nome_completo.find(' ')
nome=nome_completo[0:espaco]
print(nome)
print(nome_completo.replace(' ','#'))#altera todos que você indicar na letra/caracter que for indicado
print(nome_completo.center(80,'#'))
print(nome_completo.split(' '))#faz várias quebras pelo texto