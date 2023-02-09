#1.5
from random import randint
a = int(input("a "))
min1 = 0
max1 = 0
suma1 = 0
count1 = 0
while True:
    i = randint(-a, a)
    min1 = min(min1, i)
    max1 = max(max1, i)
    if i < 0:
        suma1 += i
        count1 += 1
    elif i == 0:
        break

count2 = 0
b = int(-a/2)
s = 0
while count2<=count1:
    for i in range(b, -1):
        s += i
    count2 +=1
s = s/count2

print(min1, max1, suma1, count1)
print(s)