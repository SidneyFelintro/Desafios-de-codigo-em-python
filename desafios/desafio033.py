n1= int(input('Me diga um número '))
n2= int(input('Me diga outro '))
n3= int(input('Me diga outro '))

if n1 > n2 and n1 > n3:
    print('O número {} é o maior '.format(n1))
elif n2 > n1 and n2 > n3:
    print('O número {} é o maior '.format(n2))
else:
    print('O número {} é o maior de todos'.format(n3))