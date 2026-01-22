n = int(input('Digite um número:  '))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Diga outro número:  '))

print('''Parabéns! você achou o número de saída!
Você digitou {} números para achar a resposta.!!
a soma entre eles é {}'''.format(cont, soma))