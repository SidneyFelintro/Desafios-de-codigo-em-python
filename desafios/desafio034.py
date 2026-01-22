s= float(input('Qual o seu salario? '))
if s <= 1250:
     print('Seu aumento de salário será de: {:.3f}'.format( s*0.15 ) )
else:
     print(('Seu aumento será de {:.3f}'.format( s*0.1 ) ) )