lista = []
par = []
impar = []
c = 0
para = ''
while True:
    c += 1
    num = int(input(f'Digite o {c}° número:'))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

    para = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if para in 'N':
        break

print(f'A sua lista de números é {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de impar é: {impar}')
