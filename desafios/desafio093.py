dados = {}
gols= []
dados['nome']= str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados['nome']} jogou? '))
for c in range(0, dados['partidas']):
    partidasGols = int(input(f'Quantos gols na partida {c}? '))

    gols.append(partidasGols)
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {dados['nome']} jogou {dados['partidas']} partidas. ')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i+1} fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')