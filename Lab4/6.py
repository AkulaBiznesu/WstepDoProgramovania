x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = []
y.insert(0, x[-3:])
y.append(x[:-3])
print(y, x)