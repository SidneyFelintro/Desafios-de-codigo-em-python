lista = []
valor = 1
cont = 0
while valor != 0:
    valor = int(input('Digite um valor:\n[DIGITE 0 PARA ENCERRAR]  '))
    if valor == 0 :
        break
    cont += 1
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valores duplicados não serão adcionados.')


print(sorted(lista))

