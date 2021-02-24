num1=int(input('numero 1: '))
num2=int(input('numero 2: '))
num3=int(input('numero 3: '))

if num1>num2 and num1>3:
    maior=num1
elif num2>num3:
    maior=num2
else:
    maior=num3

#menor
if num1<num2 and num1<num3:
    menor=num1
elif num2<num3:
    menor=num2
else:
    menor=num3

print(f'maior numero: {maior}')
print(f'maior numero: {menor}')