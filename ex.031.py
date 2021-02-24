distancia=float(input('Distancia da viagem: '))
if distancia>200:
    print('Valor da passagem: R${:.2f}'.format(0.45*distancia))
else:
    print('valor da passagem: R${:.2f}'.format(0.50*distancia))