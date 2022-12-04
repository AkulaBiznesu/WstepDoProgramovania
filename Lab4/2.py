import random
u = int(input("podaj lichbe: "))
b = []
for i in range(u):
    x = random.randint(1, 10)
    b.append(x)
print(b)

u = int(input("podaj lichbe: "))
b_2 = []
for i in range(u):
    x = random.randint(5, 15)
    b_2.append(x)
print(b_2)

g = int(input("insert"))
if g in b:
    print("1 list")
elif g in b_2:
    print("2 list")
else:
    print("no")

b_3 = b+b_2
b_3.sort()
print(b_3)