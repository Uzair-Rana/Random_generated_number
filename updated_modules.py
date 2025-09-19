import random
Number = random.randrange(1, 101)
userInput = int(input("Enter a number to compare:-"))
if Number < userInput:
    print("Computer generated a number is=", Number)
    print("The number you enter is greater then randomly generated number")
elif Number > userInput:
    print("Computer generated a number is=", Number)
    print("The number you enter is lesser then randomly generated number")
else:
    print("Computer generated a number is=", Number)
    print("The number you enter is Equal to randomly generated number")
11
