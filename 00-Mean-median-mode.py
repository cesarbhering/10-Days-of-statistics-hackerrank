infoLen = int(input())
InfoArray = input()
SplitedInfoArray = list(map(int,InfoArray.split()))
SplitedInfoArray.sort() 

#Printa a média
print(sum(SplitedInfoArray)/int(infoLen))

#Printa a mediana
if infoLen % 2 == 0:
    print((SplitedInfoArray[infoLen//2]+SplitedInfoArray[(infoLen//2)-1])/2)
else: 
    print(SplitedInfoArray[infoLen//2])

#Printa a moda
DictNumerosRepetidos = {}
for number in SplitedInfoArray:
    if number in DictNumerosRepetidos:
        DictNumerosRepetidos[number] += 1
    else:
        DictNumerosRepetidos[number] = 1
numeros_populares = sorted(DictNumerosRepetidos, key = DictNumerosRepetidos.get, reverse=True)
print(numeros_populares[0])