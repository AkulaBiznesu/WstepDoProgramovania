x = str(input("Is there a bus? Enter Y/N:" ))
y = str(input("Is it raining? Enter Y/N:" ))
if y == "Y" and x == "Y":
    print("take an umbrella and bus")
elif y == "Y" and x == "N":
    print("You won`t be at class today")
elif y == "N" and x == "Y":
    print("you`ll come to the University and the weather is great")