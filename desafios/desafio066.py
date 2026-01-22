cont = soma = 0

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    soma += n
    cont += 1
print('Parabéns, você achou a saída!')
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma ))