import random

sort = random.randint(0,5)
tentativas = 0
print('Pensei em um número!')
print(sort)
num = int(input('Agora me diga um número! '))

while num != sort:
    num = int(input('Você errou! Tente novamente!\n Diga um número! '))
    tentativas += 1

if num == sort:
    print('Os números são iguais! Você venceu!\n Você tentou {} vezes!'.format(tentativas))

