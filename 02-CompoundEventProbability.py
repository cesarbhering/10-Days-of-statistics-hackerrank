X = ['Red', 'Red', 'Red', 'Red', 'Black', 'Black', 'Black']
Y = ['Red', 'Red', 'Red', 'Red', 'Red', 'Black', 'Black', 'Black', 'Black']
Z = ['Red', 'Red', 'Red', 'Red', 'Black', 'Black', 'Black', 'Black']

# Chance de tirar red em cada pote
ChanceRedX = X.count('Red')/len(X)
ChanceRedY = Y.count('Red')/len(Y)
ChanceRedZ = Z.count('Red')/len(Z)

# Chance de tirar black em cada pote
ChanceBlackX = X.count('Black')/len(X)
ChanceBlackY = Y.count('Black')/len(Y)
ChanceBlackZ = Z.count('Black')/len(Z)

#Multiplica as pobrabilidades em cada um dos cenários que queremos, depois soma essas probabilidades.
Resultado = (ChanceRedX*ChanceRedY*ChanceBlackZ)+(ChanceRedX *
                                              ChanceBlackY*ChanceRedZ)+(ChanceBlackX*ChanceRedY*ChanceRedZ)

print(Resultado)