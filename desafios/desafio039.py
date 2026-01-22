from datetime import date

atual = date.today().year

nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif 18 < idade:
    saldo = 18- idade
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
elif 18 > idade:
    saldo = idade- 18
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
