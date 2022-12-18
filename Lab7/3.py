import numpy as np

a = np.zeros((3, 3))
# a[1:,:2]=1
#a[:,2]=1
# a[:2, :]
# a[:2, 0]=1
a[:2, [0, 2]]=1
print(a)
