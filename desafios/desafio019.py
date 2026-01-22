from random import choice

lista = []

for c in range(1,5):
    n = str(input(f'Qual o nome do {c}º aluno: '))
    lista.append(n)

escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')