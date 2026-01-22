c = total = produtos =  0
prosseguir = ''
while True:
    c += 1
    produto = str(input('Digite o nome do {}º produto: '.format(c)))
    preco = input('Digite o valor do {}º produto: '.format(c))
    total += preco

    while prosseguir not in 'SN':
        prosseguir = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if prosseguir in 'S':
            print('Ok! Vamos prosseguir!')
            break
        else:
            break
    print('Está dando certo!')

    if preco > 1000:
        produtos += 1



print(f'O valor total da sua compra é {total}.')
print(f'{produtos} foram maiores que 1000 reais.')
#ESTÁ IMCOMPLETO