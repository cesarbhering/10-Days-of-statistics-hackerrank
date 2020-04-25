from math import factorial
# A PROBABILIDADE DE UM PISTAO ESTAR COM O TAMANHO ERRADO É DE 12%.
n = 0.12


def BinomialDistribution(totalPistoes, sucessos, probDefeituosos):
    return ((factorial(totalPistoes)) / ((factorial(sucessos)) *
                                         factorial(totalPistoes-sucessos))) * (probDefeituosos**sucessos) * \
        ((1 - probDefeituosos)**(totalPistoes-sucessos))


# CALCULA E PRINTA AS POSSIBILIDADE DE TERMOS 0 ESTRAGADO, 1 ESTRAGADO OU 2 ESTRAGADOS
resultadoMax2 = 0
for i in range(0, 3):
    resultadoMax2 += BinomialDistribution(10, i, n)
print(round(resultadoMax2, 3))

# CALCULA E PRINTA A POSSIBILIDADE DE TERMOS 0 ESTRAGADO E 1 ESTRAGADO.
# NA HORA DE PRINTAR SUBTRAÍMOS O RESULTADO DE 1,
# PARA ASSIM TERMOS O VALOR DAS DEMAIS PROBABLIDADES SOMADAS,
# QUE SÃO AS QUE QUEREMOS, DE 2 ATÉ 10 ESTRAGADOS.
resultadoMin2 = 0
for i in range(0, 2):
    resultadoMin2 += BinomialDistribution(10, i, n)
print(round(1-resultadoMin2, 3))
