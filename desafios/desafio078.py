numeros = []
cont = 0

while cont < 5:
    num = int(input('Digite um valor inteiro: '))
    numeros.append(num)
    cont += 1
print('Os números da lista são: ', numeros )
print(f'O maior valor foi {max(numeros)} e menor valor foi {min(numeros)}.')
pos_maior = numeros.index(max(numeros))+1
pos_menor = numeros.index(min(numeros))+1

print('A posição do menor número é {}º'.format(pos_menor))
print('A posição do maior número é {}º'.format(pos_maior))