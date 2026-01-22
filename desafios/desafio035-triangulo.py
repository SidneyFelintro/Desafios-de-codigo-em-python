l1= int(input('digite um lado '))
l2= int(input('digite outro lado '))
l3= int(input('digite outro lado '))

if l1<l2+l3 and l2<l3+l1 and l3<l2+l1:
    print('É possível formar um triângulo ')
else:
    print('Não é possível formar um triângulo')