lado1=int(input('lado a: '))
lado2=int(input('lado b: '))
lado3=int(input('lado c: '))

if lado1==lado2 or lado2==lado3 or lado1==lado3:
    print('é possivel formar um triangulo')
elif lado1==lado2 and lado1==lado3:
    print(' é possivel formar um triangulo')
else:
    print('não é possivel formar um triangulo')
