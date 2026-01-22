numeros = ()
pares = ()
cont = n9 =  0
print("Digite números inteiros. ")
while True:
    if cont == 4:
        break
    num = int(input("Digite um número: "))
    numeros = numeros + (num,)
    cont = cont + 1

    if num == 9:
        n9 += 1
    if num % 2 == 0:
        pares += (num,)


print("Os números digitados foram:", numeros)
print(f'Há um total de {n9} números 9.')
if 3 in numeros:
    print(f'O primeiro valor 3 está na posição {numeros.index(3)+1}ª')
print(f'Os números pares foram:', pares)

