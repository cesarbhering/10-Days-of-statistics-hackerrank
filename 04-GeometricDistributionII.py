prob = float(1/3)
trys = int(5)
result = 0

for i in range(trys):
    result += prob*(1 - prob)**(int(i))

print(round(result,3))