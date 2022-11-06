a = int(input("number "))
while a != 0:
    if a < 0:
        print("negative number", a)
        break
    a = int(input())
else:
    print("negative numbers is missing")