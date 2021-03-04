jogar=input('Tem coragem de jogar jokenpo comigo? ').lower()
if jogar=="sim":
    from random import randint
    from time import sleep
    opcoes=['','pedra','papel','tesoura']
    cpu=randint(1,3)
    player=int(input('1-pedra|2-papel|3-tesoura|\n escolha: '))
    sleep(1)
    print('jo')
    sleep(1)
    print('ken')
    sleep(1)
    print('po')
    sleep(1)
    if cpu==1 and player==3 or cpu==2 and player==1 or cpu==3 and player==2:
       print(f'joguei {opcoes[cpu]}, voce {opcoes[player]}. You lose')
    elif cpu==player:
        print(f'joguei {opcoes[cpu]}, voce {opcoes[player]}. Empate!')
    else:
       print(f'joguei {opcoes[cpu]}, voce {opcoes[player]}. Parabéns voce ganhou')
else:
    print('Seu medroso')