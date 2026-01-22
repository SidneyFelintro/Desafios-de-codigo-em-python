cont = media = sum = 0
woman = []
cadastro = {}
pessoas = []

while True:

    cont += 1
    nome = str(input('Nome: '))
    cadastro['idade'] = int(input('Idade: '))
    sum += cadastro['idade']

    while True:
        cadastro['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if cadastro['sexo'] == 'F':
            woman.append(nome)
        if cadastro['sexo'] in 'FM':
            break
        print('Erro! Digite apenas F ou M!')

    while True:
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite apenas S ou N!')
    pessoas.append(cadastro.copy())
    if continuar == 'N':
        break

print('=-'*30)
print(f'A quantidade de cadastrados foi de {cont} pessoas')
media = sum / cont
print(f'A média de idade foi de {media:5.2f} anos')
print('A lista de mulheres é: ', woman)

for p in pessoas:
    if p['idade'] >= media:
        print('      ')
        for k, v, v2 in p.items():
            print(f'{k}: {v}', end=' ')
        print()

print('=-' * 30)
