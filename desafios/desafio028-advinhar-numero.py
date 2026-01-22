import random

sort = random.randint(0,5)

print('Pensei em um número!')
num = int(input('Agora me diga um número!'))

if num == sort:
    print('Os números são iguais! Você venceu!')
else:
    print('Você perdeu!')
