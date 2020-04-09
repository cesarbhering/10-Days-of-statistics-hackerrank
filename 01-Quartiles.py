NumElements = int(input())
Elements = list(map(int, input().split()))
Elements.sort()

#Pega a Mediana
if NumElements % 2 == 0:
    medianX = (Elements[NumElements//2]+((Elements[(NumElements//2)-1])))/2
else:
    medianX = Elements[(NumElements//2)]

ListmedianL =[]
ListmedianU =[]
for i in Elements:
    if i < medianX:
        ListmedianL.append(i)
    elif i > medianX:
        ListmedianU.append(i)

#Pega a MedianaU
if (len(ListmedianU)) % 2 == 0:
    medianU = (ListmedianU[len(ListmedianU)//2]+((ListmedianU[(len(ListmedianU)//2)-1])))/2
else:
    medianU = ListmedianU[(len(ListmedianU)//2)]

#Pega a MedianaL
if (len(ListmedianL)) % 2 == 0:
    medianL = (ListmedianL[(len(ListmedianL))//2]+((ListmedianL[(len(ListmedianL)//2)-1])))/2
else:
    medianL = ListmedianL[(len(ListmedianL)//2)]


print(int(medianL))
print(int(medianX))
print(int(medianU))
