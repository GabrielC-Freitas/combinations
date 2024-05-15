import csv
from itertools import chain, combinations

termos = ['TFL', 'TPA', 'TVS', 'TA', 'TLX', 'TFO', 'TB']

# Gerar todas as combinações possíveis
todas_combinacoes = list(chain.from_iterable(combinations(termos, r) for r in range(len(termos) + 1)))

# Escrever as combinações no arquivo CSV
with open('combinacoes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Combinação"])

    for combinacao in todas_combinacoes:
        writer.writerow([', '.join(combinacao) if combinacao else "Nenhum termo selecionado"])
