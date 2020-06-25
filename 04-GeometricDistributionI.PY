prob = float(1/3)
trys = int(5)

result = prob*(1 - prob)**(trys-1)

print(round(result,3))