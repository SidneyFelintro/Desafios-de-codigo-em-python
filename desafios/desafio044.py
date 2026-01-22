preco = float(input('Qual o valor da sua compra? '))
pagamento = int(input('''Qual a sua forma de pagamento?
  [1] Pagamento à vista dinheiro/cheque
  [2] Pagamento à vista no cartão
  [3] Pagamento em 2x no cartão
  [4] Pagamento em 3x no cartão 
   '''))

if pagamento == 1:
    print('Sua compra deu R${}'. format(preco * 0.9))
elif pagamento == 2:
    print('Sua compra deu R${}'.format(preco * 0.95))
elif pagamento == 3:
    print('Sua compra deu R${}'.format(preco))
elif pagamento == 4:
    print('Sua compra deu R${}'.format(preco * 1.2))
else:
    print('Sua forma de pagamento não foi aceita.')