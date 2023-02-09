#4.2
def suma(a, b, c):
    s = 0
    for i in range(a, b+1):
        s += i
    if s < c:
        return True
    else:
        return False

a = int(input("a "))
b = int(input("b "))
c = int(input("c "))

print(suma(a, b, c))
