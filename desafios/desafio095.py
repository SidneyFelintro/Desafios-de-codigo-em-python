jogadores = []

while True:
    jogador = {}
    partidas = []

    jogador['nome'] = input('Nome do jogador: ')
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(total):
        partidas.append(int(input(f'  Quantos gols na partida {i}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador)

    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('-=' * 30)
print(f'{"cod":<5}{"nome":<15}{"gols":<20}{"total":<5}')
print('-' * 50)

for i, j in enumerate(jogadores):
    print(f'{i:<5}{j["nome"]:<15}{str(j["gols"]):<20}{j["total"]:<5}')

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('Erro! Jogador não existe.')
    else:
        print(f'-- Levantamento do jogador {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i} fez {g} gols.')

