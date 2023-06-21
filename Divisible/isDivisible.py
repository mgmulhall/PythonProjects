#Maggie Mulhall
#This program will accept two numbers and return True if one is divisible by the other
#Only whole, positive integers will be accepted

#Import libraries to utilize While loop
from ast import While

def isDivisible():
    print('\nPlease enter 2 whole, positive integers to see if one is divisible by the other.')

    while True:
        #Prompt user for input
        first = input("Enter first number: ")
        second = input("Enter second number: ")
        
        #Validate user input meets requirements
        if first.isdigit() and int(first)>0 and second.isdigit() and int(second)>0:
            break
        print("Sorry, both numbers need to be whole, positive integers. Try again!")

    #Convert inputs to integers
    first=int(first)
    second=int(second)

    #Check if first number divides by second, if so return true
    if(first%second==0):
        return True
    #Check if second number divides by first, if so return true
    elif (second%first==0):
        return True
    else: 
        return False

#Call isDivisible function and print out the result
print(isDivisible())
