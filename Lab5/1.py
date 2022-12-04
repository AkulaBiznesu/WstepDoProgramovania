values = [10, 20, 30]
keys = ["ten", "twenty", "thirty"]
dict1 = {}

# z = zip(keys, values)
# print(list(z))

# dict1 ={keys[i]:values[i]  for i in range(len(keys))}

for i in range(len(keys)):
    dict1[keys[i]] = values[i]
print(dict1)

dict_2 = {"thirty":30, "foutry":40, "fifty":50}
print(dict_2)

dict_3 = dict1.copy()
dict_3.update(dict_2)
print(dict_3)