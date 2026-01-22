maiores_18 = mulheres_menos_20 = homens = c = 0

while True:
    c += 1
    sexo =  ' '
    prosseguir = ' '
    while True:
        idade = input('Digite a idade da {}ª pessoa: '.format(c))
        if idade.isdigit():
            idade = int(idade)
            break
        else:
            print('Idade invalida! tente novamente.')
    while sexo not in 'FM':
        sexo = str(input('Agora me diga o sexo da {}ª pessoa: [F/M]'.format(c))).upper().strip()[0]
        if sexo not in 'FM':
            print('Sexo invalido! tente novamente.')
        else:
            break
    print(f'{c}ª pessoa cadastrada com sucesso!')

    while prosseguir not in 'SN':
        prosseguir = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if prosseguir not in 'SN':
            print('Resposta não aceita! tente novamente.')
        else:
            break
    if idade >= 18:
        maiores_18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    if prosseguir == 'N':
        break

print('NOS SEUS CADASTROS HÁ: ')
print('{} pessoas maiores de 18 anos'.format(maiores_18))
print('{} homens cadastrados'.format(homens))
print('{} mulheres com menos de 20 anos'.format(mulheres_menos_20))
print('FIM')



