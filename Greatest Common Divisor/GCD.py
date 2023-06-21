#Maggie Mulhall
#This program finds the greatest common divisor of two integers

#Input:
# Two Positive Integers
#Output:
# Greatest Common Divisor of Inputs

def GCD(first,second):
    if(second==0):
        return first
    else: 
        return GCD(second,first%second)

answer=GCD(111, 378)
print("GCD: ",answer)