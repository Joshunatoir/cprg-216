continue_program = "y"

numberStorage = []
devideby = 0
proceed = 1
while continue_program == "y":  
    
    while proceed == 1 :
        numbergetter = (input("Please enter a number to be averaged: "))
        try:
            numbergetter = float(numbergetter)
            print("i got a number ", numbergetter)
            numberStorage.append(numbergetter)
        except:
            print("I got a str")
            proceed = input("would you like to stop?(no:1): ")
        print("this is my list",numberStorage)
    
    additioned = sum(numberStorage)
    
    divisor = len(numberStorage)

    average = additioned/divisor

    
    print ("this is the average: ", average)
    

    print("it finished")
    continue_program = input("Would you like to go again?(Y): ")
    # devideby=len(numberStorage)
    # sumOfNumbers = sum(numberStorage)
    # average = sumOfNumbers/devideby
    

    # print("the average of the ", devideby, " numbers you entered is ",average)
    # continue_program = input ("to try again please enter 'y' anything else will end the loop: ")
    # if continue_program == "y":
    #     proceed = "y"