lista = []
c = 0
contador = 0
while True:
    c += 1
    valor = int(input(f'Digite o {c}° valor: '))
    lista.append(valor)

    if valor == 5:
        contador += 1

    para = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if para in 'N':
         break
    elif para == 'S':
     print('OK!\n')
    else:
        print('Comando inválido! Programa encerrado!\n')
        break

decrescente = sorted(lista, reverse=True)

print(f'Sua lista contém {len(lista)} elementos e é formada pelos seguintes elementos:{decrescente}')
print(f'O número 5 foi digitado {contador} vezes.')


