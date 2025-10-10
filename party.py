import os, time
# this is a party code thing?
os.system('cls')
print("hello , welcome to a party where only people above the age of 18 are allowed in")

age = int(input("What is your age in years?:YY"))

gendr = input("what are you Male or Female?:M/F")


if age >= 18:
    
    print ("welcome to the party, come on in and enjoy your self, no drinks are served due to low budget")
    time.sleep(1)
    if gendr == "M":
        print("BTW the Mens room is on your left down the hall there")
        time.sleep(1)
    elif gendr == "F":
        print("BTW the Ladies room is on your right down the hallway over there.")
        time.sleep(1)
elif age <= 18:
    retrn = (18 - age)

    print("please come back in", retrn,"years, and you will be welcome to join the party!")





