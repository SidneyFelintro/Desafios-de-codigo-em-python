c = 0
n = int(input('Você uer a tabuada de qual número? '))
print(f'A TABUADA DE {n} É:')
print('-='*10)
while c < 10:
    c += 1
    print(f'{n:<1} x {c:<3} = {n*c} ')
print('-='*10)
