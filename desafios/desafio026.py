word = str(input('Digite uma frase: ')).upper()
print('sua frase tem {} letras A'.format(word.count('A')))
print('o primeiro A se encontra na posição {}'.format(word.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(word.rfind('A') + 1))