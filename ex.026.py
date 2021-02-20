#conta qtd de A em uma frase
frase=input('digite uma frase: ').strip().lower()
print('essa frase contem {} letras A'.format(frase.lower().count('a')))
print('o primeiro a aparece no caractere {}, e o ultimo {}'.format(frase.find('a'),frase.rfind('a')))