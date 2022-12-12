a = []
nc=6
nr=6
a = [[i%2 for i in range(nc)] for r in range(nr)]
for r in a:
     print(*r)