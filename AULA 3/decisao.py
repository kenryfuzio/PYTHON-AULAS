from os import system
system('cls')
numero = input('informe um número: ')
if(numero.isnumeric()==True):
    print('isto é um número')
    numero=int(numero)
    if(numero % (2) == 1): #% = módulo(mod)
        print("Este é um número ímpar")
    else:
        print("Este é um número par")

else:
    print('Isto não é um número')
print('final do código')