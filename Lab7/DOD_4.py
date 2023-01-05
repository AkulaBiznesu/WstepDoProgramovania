import numpy as np
array = np.zeros((5, 5))
array[0:, :1] = 1
array[4:, 0:] = 1
array[0, :5] = 1
array[:5, 4] = 1
print(array)
# def switch(*args):
#     for i in args:
#         if i == 1:
#             i = i-1
#         elif i == 0:
#              i = i + 1

#
# new_array = switch(array)
# print(new_array)