from random import randint
v= 0
while True:
    
    sort = randint(0, 10)
    
    while True:
        entrada = input('Me diga um número de 0 a 10 para o nosso impar ou par! ')
        if entrada.isdigit():
            jogador = int(entrada)
            if 0 <= jogador <= 10:
                break
            else:
                print('Valor inválido! Deve ser um número entre 0 e 10. Tente novamente.')
        else:
            print('Valor inválido! Você deve digitar apenas números. Tente novamente.')

    resultado = sort + jogador
    escolha = ' '

    while escolha not in 'PI':
        escolha = input('Você quer ser impar ou par? [I/P]').upper().strip()[0]
        if escolha == 'I':
            computador = 'P'
            break
        elif escolha == 'P':
            computador = 'I'
            break
        else:
            print('Essa escolha não está disponível! ')

    if escolha == 'P':
        if resultado % 2 == 0:
            print('Parabéns!! Você venceu! ')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if resultado % 2 == 1:
            print('Parabéns!! Você venceu! ')
            v += 1
        else:
            print('Você perdeu!')
            break

    print('DEU PAR!'if resultado % 2 ==0 else 'DEU IMPAR!')
    print('Vamos novamente! ')
    print('-=' * 20)

print(f'GAME OVER! VOCÊ PERDEU. VOCÊ GANHOU {v} VEZES ')






