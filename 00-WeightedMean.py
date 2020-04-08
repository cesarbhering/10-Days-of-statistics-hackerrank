NumElments = int(input())
Elements = list(map(int, input().split()))
WeightElements = list(map(int, input().split()))


calc = (sum(list(Elements[i]*WeightElements[i] for i in range (0, len(Elements))))/(sum(WeightElements)))

print(round(calc,1))