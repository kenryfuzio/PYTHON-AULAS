from os import system
system('cls')

#programa para mostrar números inteiros em extenso
#somente números de 1 a 100
centenas = ["", "cem", "duzentos", "trezentos", "quatrocentos", ]
dezenas = ["","dez", "vinte", "trinta" , 
"quarenta", "cinquenta", "sessenta", "oitenta" , 
"noventa"]
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
"dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")
valor = input("informe um número de 1 a 99: ")
numerico=int(valor)
extenso=''
if(numerico < 20):
    #print(numeros[numerico])
    extenso = numeros[numerico]
elif(numerico < 100):
    #print(valor[0:1])
    #print(dezenas[int (valor[0:1])],"e", numeros[int(valor[1:2])])
    extenso = dezenas[int(valor[0:1])]
    if(valor[1:2]!='0'):
        extenso = f"{extenso} e {numeros[int(valor[1:2])]}"
print(extenso)
