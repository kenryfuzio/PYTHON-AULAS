"""
 Calcular área do retângulo        

"""
print('***Calculo da da area do retangulo***\n\nInforme o primeiro lado')
#print('Informe o primeiro lado:')
lado1=input()
print('Informe o segundo lado: ')
lado2=input()
#variavel isnumeric=verifica se a variavel pode ser um número inteiro
#variavel isdecimal=verifica se a variável pode ser um número com casas decimais
print("O primeiro valor é número?", lado1.isnumeric())
print("O primeiro valor é número?", lado2.isnumeric())
print("Será que vai dar certo ou vai dar errado?")
# int= transforma o valor da variável em inteiro
# float= transforma o valor da variável em float(decimal)
area = int(lado1) * int(lado2)
print('A area do retangulo é {} m² sendo os lados de {} x {}'.format(area, lado1, lado2))
print("A area do retângulo é", area, "m² sendo os lados de", lado1, 'x', lado2)
