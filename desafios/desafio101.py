def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))