import math
n = int(input("Введите натуральное n: "))
i = 1
for i in range(1,n + 1):
    a = (i - 1)/(i + 1) + math.sin(pow((i - 1),3)/(i + 1))
    i += 1
    if a > 0:
        print(a)
