x = int(input("How old are you: "))
if x < 4:
   print("Free entrance")
elif 4 < x < 18:
   print("ticket cost 10zl")
elif x > 18:
   print("ticket cost 20zl")
else: print("_")