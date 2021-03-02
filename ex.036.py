ano=int(input('digite um ano, ou digite 0 para o atual: '))
from calendar import isleap
bissexto=isleap(ano)
if bissexto is True:
    print('esse ano é bissexto')
else:
    print('esse ano nao é bissexto')