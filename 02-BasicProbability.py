Dice1 = [1, 2, 3, 4, 5, 6]
Dice2 = [1, 2, 3, 4, 5, 6]

results = []


for n in Dice1:
    for i in Dice2:
        results.append(n+i)

NoveEAbaixo = 0
AcimaDe9 = 0
for num in results:
    if num > 9:
        AcimaDe9 += 1
    else:
        NoveEAbaixo += 1

print(NoveEAbaixo/len(results))
