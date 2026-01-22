from random import randint


itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('O computador vendeu!')
    else:
        print('Jogada inválida')

elif computador == 1:
    if jogador == 0:
        print('O computador vendeu!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida')

elif computador == 2:
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('O computador vendeu!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')