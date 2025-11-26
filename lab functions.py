#Joshua Dyck
#November 25th, 2025
#overcomplicated lab

import random
NUM_DICE_TO_ROLL = 5
SEED = 2183
proceed = 3

def volume(length,width,height):
    box_volume = length * width * height
    return box_volume

def main_box():
    def getinput(box_num):
        while True:
            try:
                print("box #",box_num,"Length (cm):", end="")
                length = float(input())
                break
            except ValueError: #if user enters wrong type of input then it causes a value error 
                print("please try again")
        while True:
            try:
                print("box #",box_num,"Width (cm):", end="")
                width = float(input())
                break
            except ValueError:
                print("Try again")
        while True:
            try:
                print("box #",box_num,"Height (cm):", end="")
                height = float(input())
                break
            except ValueError:
                print("Try again")
        return length, width, height
    print("please insert the length, width and height for box #1") 
    l1,w1,h1 = getinput(1) 
    print("the volume of box #1 is:",f"{volume(l1,w1,h1):.2f}","ccm")
    input("continue. . .")
    print("please insert the length, width and height for box #2")
    l2,w2,h2 = getinput(2) 
    print("the volume of box #2 is:",f"{volume(l2,w2,h2):.2f}","ccm")
            
def roll_dice(NUM_DICE_TO_ROLL):
    roll_results = []
    while NUM_DICE_TO_ROLL>0:
        roll_results.append(random.randint(0,6))
        NUM_DICE_TO_ROLL -=1
    return roll_results

def most_repeats(roll_results):
    count1 = roll_results.count(1)
    count2 = roll_results.count(2)
    count3 = roll_results.count(3)
    count4 = roll_results.count(4)
    count5 = roll_results.count(5)
    count6 = roll_results.count(6)
    all_counts = [count1,count2,count3,count4,count5,count6]
    repeats = max(all_counts)
    
    return repeats

def dice_main():
    random.seed(SEED)
    
    again = "yes"
    while True:
        
        if again not in ("yes","y",'1','continue'):
            break
        else:
            results = roll_dice(NUM_DICE_TO_ROLL)
            repeats = most_repeats(results)
            if repeats == 5:
                print("Congratulations, your roll of",results,"contains",repeats,"of a kind, That means you rolled all the same!")
                break
            else:
                print("Your roll of",results,"contains",repeats,"of a kind")
            
        again = input("Do you want to roll again (Y/N)?").lower()    

while proceed >0:
    
    print("What would you like to do?")
    print("1: Roll sum dice?")
    print("2: Calculate the volume of two boxes?")
    print("3: Quit")
    choice = input(":")
    if choice in ("1","A",'a','dice'):
        dice_main()
        proceed = 3
    elif choice in ("2","B","b","box"):
        main_box()
        proceed=3
    elif proceed == 1 or choice in ("3","quit","stop","halt","cease","end","break","terminate","off","shutdown","shut-down","shut down") : #extra function with multiple ways to quit
        print("quiting program now")
        print("Good Bye")
        proceed = 0
    else:
        print("try again")
        proceed -=1
        