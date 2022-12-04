import random
grades = []
for i in range(15):
    p = random.uniform(0, 50)
    p = round(p, 2)
    grades.append(p)
print(grades)
print(f"max = {max(grades)}, min = {min(grades)}")
p = float(input("p "))
if p in grades:
    x = grades.index(p)
    print(x)
else:
    print("no")

sr = round(sum(grades)/len(grades), 2)
print(sr)

upper = []
lower = []
for i in grades:
    if i > sr:
        upper.append(i)
    elif i < sr:
        lower.append(i)
print(lower, upper)
print(len(lower), len(upper))
