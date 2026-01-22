dias =int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km o carro ficou alugado? '))
preco = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {float(preco)}')