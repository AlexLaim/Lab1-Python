from math import ceil, log
import random

n = random.randint(1,10000)
digits = [random.randint(1,10) for i in range(n)]
# nulls = pow(2, ceil(log(n, 2))) - len(digits)
[digits.append(0) for i in range(pow(2, ceil(log(n, 2))) - len(digits))]


# print("Количество элементов: "+ str(n))
# print("Количество нулей: " + str(nulls))



print(digits)