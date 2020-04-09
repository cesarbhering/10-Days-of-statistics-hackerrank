NumElements = int(input())
Elements = list(map(int, input().split()))
Elements.sort()

# Pega a média
media = sum(Elements)/NumElements

# Pega o desvio padrão
ListSquaredDistance = []
for i in Elements:
    ListSquaredDistance.append(int((i-media)**2))

Desvio = (sum(ListSquaredDistance)/NumElements)**0.5

# Mostra o Desvio Padrao
print(round(Desvio, 1))
