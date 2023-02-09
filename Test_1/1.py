#4.1
def fill(a, b, c):
    l = []
    i = 0
    while i <= a:
        for i in range(0, b+1, c):
            l.append(i)
        i+=1
    return l
a = int(input("a "))
b = int(input("b "))
c = int(input("c "))
print(fill(a, b, c))