from datetime import datetime
    

def idade (nascimento):
    idadeAnos = hoje.year - nascimento.year 
    return idadeAnos

hoje = datetime.now()
print(hoje)
print(hoje.strftime("%A %d/%B/%Y"))
nascimento = datetime(2003, 5, 2)
print(nascimento)
print(idade(datetime(2003,2,5)))
print(idade(datetime(2000,7,9)))
print
