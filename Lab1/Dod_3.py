#ax^2 + bx+c=0
import math

a = float(input("a "))
b = float(input("b "))
c = float(input("c "))
d = b**2-4*a*c

if d > 0:
    sd = math.sqrt(d)
    x_1 = -b+sd/2*a
    x_2 = -b-sd/2*a
    print(x_1, x_2)
elif d == 0:
     x = -b/2*a
     print(x)
elif d < 0:
    print("impossible")