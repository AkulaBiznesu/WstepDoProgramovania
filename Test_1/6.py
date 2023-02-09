#4.3
def rivn(x):
    if x > 0:
        return 2*x
    elif x == 0:
        return 0
    else:
        return -3*x
a = int(input("x: "))
print(rivn(a))