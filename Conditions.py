import os, math

cond = True
condTwo = False

# when ever you have a boolean variable have it in a form of a question, such as
winningSon = False
isBroke = True
male = False

expr = 3>4 # this is a comparison which results in false
os.system('cls')
print(" how old are you ")
a = int(input ("age:"))

print("you must be over 18 to pass")

overEighteen = a >= 18
os.system('cls')
if overEighteen ==(True):
    
    print("Welcome Adult")
else:
    print("Leave, you child!")

if overEighteen:
    print("this works because the variable is a boolean which is true")
else:
    print("this is returning because the variable is a boolean which is false")

#comparision operators : 
# == (is this the same value?)
# === (is this completely identical)
# > (is a larger than b)
# < (is A smaller than b)
# >= (is a larger or equal to b)
# <= (is a smaller or equal to b)

x = (math.sqrt(64))
print (x)

# you can you a boolean variable as a condition of a if statement . interesting

