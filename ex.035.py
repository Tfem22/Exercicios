lado1=int(input('lado a: '))
lado2=int(input('lado b: '))
lado3=int(input('lado c: '))

if (lado1+lado2)>lado3 and (lado2+lado3)>lado1 and (lado1+lado3)>lado2:
    print('dado as retas a,b e c, é possivel formar um trigangulo')
else:
    print('dado as retas a,b e c, não é possivel formar um triangulo')
