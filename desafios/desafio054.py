from datetime import date

cont= 0
ano= date.today().year

for c in range(1, 8):
    nasc = int(input('digite o {}º ano de nascimento: '.format(c)))
    if ano - nasc <= 18:
        cont += 1

maiores = c - cont

print(f'você informou {cont} pessoas com menos de 18 anos')
print(f'Você informou {maiores} pessoas com mais de 18 anos')





