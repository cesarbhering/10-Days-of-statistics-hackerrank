NumElements = int(input())
Elements = list(map(float, input().split()))
FrqElements = list(map(int, input().split()))

ArrayS = []
for i in range(NumElements):
    for x in range(0, FrqElements[i]):
        ArrayS.append(Elements[i])
ArrayS.sort()

#Pega a Mediana
if len(ArrayS) % 2 == 0:
    medianX = (ArrayS[len(ArrayS)//2]+((ArrayS[(len(ArrayS)//2)-1])))/2
else:
    medianX = ArrayS[(len(ArrayS)//2)]

#Pega o index do meio da tabela
s = len(ArrayS)//2

#Cria as listas de Q1 e Q3
ListmedianQ1 = ArrayS[:s]
ListmedianQ3 = ArrayS[-s:]


#Pega a mediana do Q1
if (len(ListmedianQ1)) % 2 == 0:
    medianQ1 = (ListmedianQ1[len(ListmedianQ1)//2]+((ListmedianQ1[(len(ListmedianQ1)//2)-1])))/2
else:
    medianQ1 = ListmedianQ1[(len(ListmedianQ1)//2)]

#Pega a mediana do Q3  
if (len(ListmedianQ3)) % 2 == 0:
    medianQ3 = (ListmedianQ3[(len(ListmedianQ3))//2]+((ListmedianQ3[(len(ListmedianQ3)//2)-1])))/2
else:
    medianQ3 = ListmedianQ3[(len(ListmedianQ3)//2)]

#Printa Q3-Q1, com arredondamento para um número decimal.
print(round(medianQ3-medianQ1,1))
