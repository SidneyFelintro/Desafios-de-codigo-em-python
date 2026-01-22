lista = []
mai = men = 0
primeiro = True

while True:
    nome = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso: "))

    lista.append([nome, peso])

    if primeiro:
        mai = men = peso
        primeiro = False

    else:
        if peso > mai:
            mai = peso
        if peso < men:
            men = peso

    continuar = str(input("Deseja continuar? [S/N] ")).upper()
    if continuar == "N":
        break

print(f'o número de pessoas cadastradas foi de {len(lista)}')
print(f'o maior peso cadastrado foi {mai}')
for p in lista:
    if p[1] == mai:
        print(p[0], end = ' ')
print()
print(f'o menor peso cadastrado foi {men}')
for p in lista:
    if p[1] == men:
        print(p[0], end = ' ')
print()