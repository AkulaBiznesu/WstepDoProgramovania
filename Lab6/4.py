def zad4(**kwargs):
    if "koniec" in kwargs:
            end=kwargs["koniec"]
    else:
            end= "\n"
    for i in kwargs:
        print(i, kwargs[i], end=end)

zad4(a=2, b=10, c=True, koniec=", ")
print()
zad4(a=2, b=10, c=True)