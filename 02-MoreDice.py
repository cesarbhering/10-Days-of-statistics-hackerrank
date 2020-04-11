Dice1 = [1, 2, 3, 4, 5, 6]
Dice2 = [1, 2, 3, 4, 5, 6]

results = []

for n in Dice1:
    for i in Dice2:
        results.append(n+i)

ResultadosSeisComNumerosDiferentes = 0
for n in Dice1:
    for i in Dice2:
        if n != i and n+i == 6:
            ResultadosSeisComNumerosDiferentes += 1

print(ResultadosSeisComNumerosDiferentes/len(results))
