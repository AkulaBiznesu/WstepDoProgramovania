a = "addition"
s = "subtraction"
m = "multiplication"
d = "dividing"
e = "exponentiation"
print("1)", a, "2)", s, "3)", m, "4)", d, "5)", e)

i = int(input("input number of operation: "))
x = float(input("argument 1: "))
y = float(input("argument 2: "))

if i == 1:
   print(x+y)
elif i == 2:
   print(x-y)
elif i == 3:
   print(x*y)
elif i == 4:
   print(x/y)
elif i == 5:
   print(x**y)
else: print("dumb")

