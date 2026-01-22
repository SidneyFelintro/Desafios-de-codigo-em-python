n1 = int(input('primeiro valor: '  ))
n2 = int(input('segundo valor: ' ))

opção = 0

while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    opção = int(input('Qual é a sua opção?  '))

    if opção == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opção ==2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é menor que {}'.format(n2, n1))
        else:
            print('Os números são iguais, não há maior.')
    elif opção == 4:
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))

    elif opção == 5:
        print('Saindo do programa')
    else:
        print('Opção invalida! Tente novamente!')

print('Fim do programa! Volte sempre!')
