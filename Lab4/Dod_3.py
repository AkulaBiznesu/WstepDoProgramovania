import numpy as np
# a = []
# nc=6
# nr=6
# a = [[i%2 for i in range(nc)] for r in range(nr)]
# for r in a:
#      print(*r)

Z = np.zeros((8,8), dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)