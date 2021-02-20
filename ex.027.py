#1° e ultimo nome
NomeCompleto=str(input('digite seu nome completo: ')).title().strip().split()
print('seu primeiro nome é: {} \nE seu ultimo nome é: {}'.format(NomeCompleto[0],NomeCompleto[-1]))