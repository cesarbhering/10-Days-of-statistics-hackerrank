from math import factorial
# RAZAO MENINO PRA MENINA É 1.09 : 1. POR ISTO COLOCAMOS A LISTA [1.09, 1].
n = [1.09, 1]


def BinomialDistribution(totalFilhos, sucessos, probMenino):
    return ((factorial(totalFilhos)) / ((factorial(sucessos)) *
                                        factorial(totalFilhos-sucessos))) * (probMenino**sucessos) * \
        ((1 - probMenino)**(totalFilhos-sucessos))


# CALCULA AS POSSIBILIDADE DE TERMOS 0 MENINO, 1 MENINO E 2 MENINOS
# (QUE É OQ UE NÃO QUEREMOS QUE ACONTEÇA).
resultado = 0
for i in range(0, 3):
    resultado += BinomialDistribution(6, i, (n[0] / (n[0]+1)))

# NA HORA DE PRINTAR SUBTRAÍMOS O RESULTADO DE 1,
# PARA ASSIM TERMOS O VALOR DAS DEMAIS PROBABLIDADES SOMADAS,
# QUE SÃO AS QUE QUEREMOS, DE 3 ATÉ 6 FILHOS HOMENS.
print(round(1-resultado, 3))
