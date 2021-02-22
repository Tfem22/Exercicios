#advinhar numero
from random import randint
num=randint(0,5)
chute=int(input('Qual numero voce acha q eu pensei? '))

if chute==num:
    print('parabens voce acertou :)')
else:
    print('voce errou ;-;')
