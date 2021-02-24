salario=float(input('digite o salario: '))
if salario>1250:
    salario=salario*1.1
    print('o salario com aumento de 10%: R${:.2f}'.format(salario))
else:
    salario=salario*1.15
    print('o salario com aumento de 15%: R${:.2f}'.format(salario))