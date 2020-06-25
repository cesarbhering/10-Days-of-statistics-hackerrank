# P(x = k) = ((e**-u)*(u**k)) / K!

e = 2.71828  # Constante Natural
u = 2.5
x = 5
Kfat = 1

# Faz a fatoração do denominador
for i in range(1, x+1):
    Kfat *= i


result = ((e)**(-u)*(u**x)) / Kfat

print(round(result, 3))
