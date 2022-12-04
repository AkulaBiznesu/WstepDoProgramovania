sample_dict = {
"name": "Kelly",
"surname": "Jones",
"age": 25,
"salary": 8000,
"city": "New york"}
for k, v in sample_dict.items():   # ("name", "Kelly"),
    print (f'{k:<10} = {v:>10}')

M = {}
L = ["age", "name"]
for key in L:
    if key in sample_dict:
        M[key] = sample_dict[key]
print(M)