Paus = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
Espada = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
Ouros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
Copas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

TamanhoBaralho = len(Paus)+len(Espada)+len(Ouros)+len(Copas)

# Nossas possibilidades na primeira carta são do tamanho do baralho,
# pois podemos pegar de qualquer naipe.
Carta1 = TamanhoBaralho/TamanhoBaralho
# Agora com uma carta na mão, estamos retritos a apenas 1 naipe (paus como exemplo),
# e também devemos considerar que temos menos 1 carta dele no baralho.
Carta2 = (len(Paus)-1)/(TamanhoBaralho-1)
print(Carta1*Carta2)
