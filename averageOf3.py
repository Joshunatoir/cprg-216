continue_program = "y"

while continue_program == "y":  

    num2 = int(input ("please enter second number to be averaged: "))
    num3 = int(input ("please enter third number to be averaged: "))
    num1 = int(input ("please enter first number to be averaged: "))

    average = (num1 + num2 + num3)/3
    print("the average of the 3 numbers you entered is ",average)
    continue_program = input ("to try again please enter 'y' anything else will end the loop: ")