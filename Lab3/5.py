n = int(input("How many students in the class? "))
i = 1
suma = 0
while i <= n:
    x = int(input(f"mark:{i}"))
    i = i+1
    suma = suma + x
sred = suma/n
print(sred)

