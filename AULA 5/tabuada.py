from os import system, name
#if ternario(if escrito em uma linha só, não pode ter elif)
system('cls') if(name=='nt') else system('clear')
#igual ao comando de cima
if(name=="nt"):
    system('cls')
else:
    system('clear')
tabuada = 5
for i in range(11):
    #print('{} x {} = {}' .format(tabuada,i, tabuada *i))
    print(f"{tabuada: >4} x {i:>4} = {tabuada * i:>4}")
    #print(tabuada, 'x', i, '=', tabuada* i)