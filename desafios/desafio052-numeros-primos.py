n = int(input('Digite um número: '))

divisores = 0

print(f'\nAnalisando o número {n}...')
print('-' * 30)

for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[32m{c}\033[0m', end=' ')
        divisores += 1
    else:
        print(f'\033[31m{c}\033[0m', end=' ')

print(f'\n\nO número {n} foi divisível {divisores} vezes.')

if divisores == 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO.')