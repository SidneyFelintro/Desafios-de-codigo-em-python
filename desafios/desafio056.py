soma= 0
maior = 0
menor = 0
nome_mais_velho = []
cont = 0
mulher_mais_nova = []

for c in range(1, 5):
    print('-' * 5, '{}º pessoa'.format(c), '-' * 5)
    nome = str(input('Digite o {}º nome: '.format(c))).strip().title()
    idade = int(input('Digite a {}º idade: '.format(c)))
    sexo = str(input('Digite o {}º sexo[M/F]: '.format(c))).upper().strip()

    soma +=idade

    if c == 1:
        maior = idade
        menor = idade
        nome_mais_velho = [nome]
        mulher_mais_nova = [sexo]

    else:
        if idade > maior and sexo == 'M':
            maior = idade
            nome_mais_velho = [nome]

        elif idade < menor:
            menor = idade

            if idade < 20 and sexo == 'F':
                mulher_mais_nova = [sexo]
                cont += 1

        elif idade == maior:
            nome_mais_velho.append(nome)

print('A média de idade é de {:.2f}'.format(soma/4))
print('A maior idade é {}'.format(maior))
print('o nome do homem mais velho é {}'.format(', '.join(nome_mais_velho)))
print('A quantidade de mulheres com menos de 20 anos foi de {}'.format(cont))

