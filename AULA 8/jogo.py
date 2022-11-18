from os import system, name
import random
jogo = 's'
while(jogo.lower() == 's'):
    system('cls') if (name=='nt') else system('clear')
    print("jogo:Papel, Pedra e Tesoura".center(80,'*'))
    print('\Escolha a sua opção de jogada:')
    print('[0] Papel\n[1] Pedra\n[2] Tesoura\n')
    jogada=input('-> ')
    jogada = int(jogada)
    computador = random.randint(0,2)
    opcoes = ["Papel", "Pedra", "Tesoura"]
    resultado = [["Empate!","Você Ganhou!","Você Perdeu!"],
                 ["Você Perdeu!","Empate!","Você Ganhou!"],
                 ["Você Ganhou!","Você Perdeu!","Empate!"]]
    
    print(resultado[jogada][computador])
    print(f'Você ->{opcoes[jogada]} X {opcoes[computador]} <- Computador')


    jogo = input('\nDeseja jogar novamente? Aperte "s" para continuar ')