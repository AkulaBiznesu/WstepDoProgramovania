x = int(input("x= "))
y = int(input("y= "))
for n in range(x, y, 1):
    print(n)
if x > y:
    for n in range(y, x, 1):
        print(n)
