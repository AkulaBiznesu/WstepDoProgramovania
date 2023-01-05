def funk (string):
    slovnik = {}
    for i in string:
        if i in slovnik:
             slovnik[i] = slovnik[i]+1
        else:
            slovnik[i] = 1
    return slovnik
print(funk("anihilator"))
