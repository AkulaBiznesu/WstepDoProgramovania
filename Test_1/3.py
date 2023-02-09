#1.4
from random import randint
a = int(input("a "))
b = int(input("b "))
n = int(input("n "))
count= 0
suma = 0
for i in range(a, b):
    n = randint(0, n)
    if i % 3 != 0 and i in range(a, b):
        count += 1
        # print(i)
    else:
        suma += i
print(f"не ділиться на 3: {count}")
print(f"сума решти: {suma}")
