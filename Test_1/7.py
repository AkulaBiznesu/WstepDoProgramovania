#4.4,  4.6
def zad(a, b):
    l = []
    while a<=b:
        l.append(a)
        a+=1
    return l

a = int(input("a "))
b = int(input("b "))

print(zad(a, b))