x = int(input("x "))
y = int(input("y "))
z = int(input("z "))

if x<=y<=z:
    print(x, y, z)
elif y<=x<=z:
    print(y, x, z)
elif z<=y<=x:
    print(z, y, x)
elif x<=z<=y:
    print(x, z, y)
elif y<=z<=x:
    print(y, z, x)
if z<=x<=y:
    print(z, x, y)

