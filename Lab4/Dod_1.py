import random
u = int(input("podaj lichbe: "))
b = []
c = []
for i in range(u):
    x = random.randint(1, 50)
    b.append(x)

u = int(input("podaj lichbe: "))
b_2 = []
for i in range(u):
    x = random.randint(1, 60)
    b_2.append(x)

c = b+b_2
c.sort()
print(c)