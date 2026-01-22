lista = []
cont = 0

while True:
    cont += 1
    nome = str(input(f'Qual o nome do {cont}º aluno? '))
    nota1 = float(input(f'Qual a 1ª nota do aluno? '))
    nota2 = float(input(f'Qual a 2ª nota do aluno? '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])


    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if  opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<< VOLTE SEMPRE >>>')


