casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário R$'))
tempo = int(input('Em quantos anos você vai pagar sua casa? '))
prestacao= casa/(tempo * 12)

if prestacao >= (salario * 1.3):
    print('A prestação é maior que 30% do seu salário')
else:
    print('Sua prestação é de R$ {:.3f} por {} anos' .format(prestacao, tempo))
#print(prestacao)