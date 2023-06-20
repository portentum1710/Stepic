cities = list(map(str, input().split()))

lenth = len(cities)

i = 0
while i < lenth:
    if len(cities[i]) < 5:
        print("НЕТ")
        break
    i += 1
else:
    print("ДА")

