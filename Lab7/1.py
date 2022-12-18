import numpy as np
a = range(7, -1, -1)
b = [2**i for i in a]
print(b)
wagi = np.array(b)
print(wagi)

liczba_bin = np.random.randint(low=0, high=2, size=8)
print(liczba_bin)
c = liczba_bin*wagi
print(c)
print(c.sum())

