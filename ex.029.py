velocidade=int(input('Velocidade Km: '))
if velocidade>80:
    multa=10*(velocidade-80)
    print('Limite ultrapassado, sua multa é de: R$ {}'.format(multa))
else:
    print('Voce estava dentro do limite')