nome= str(input('Qual o seu nome completo? '))

print(f'Seu nome com todas as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas é: {nome.lower()}')

nome1 = ''.join(nome.split())
print(f'A quantidade de letras no seu nome é: {len(nome1)}')

nome2=nome.split()
print(f'A quantidade de letras no seu primeiro nome é: {len(nome2[0])} ')


#Esse código está contando os espaços. Rever.