dicionario = {}

dicionario['nome'] = str(input('Nome: '))
dicionario['media'] =  float(input(f'Média de {dicionario["nome"]}: ?'))

if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
elif 5 <= dicionario['media'] <= 6.9:
    dicionario['situacao'] = 'Recuperação'
else:
    dicionario['situacao'] = 'Reprovado'
print('-')
for k, v in dicionario.items():
    print(f'  -{k} é igual a {v}')

