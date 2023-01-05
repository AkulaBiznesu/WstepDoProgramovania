def potega(list1, list2):
    list3 = []
    for i in range(len(list1)):
        x = list1[i] ** list2[i]
        list3.append(x)
    return list3
print(potega([1,2,3,4,5], [6,7,8,9,10]))
