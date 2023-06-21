#Maggie Mulhall
#This program calculates the number of digits of a number in binary

#Input: Integer
#Output: Number of digits in the binary expansion of input
def binary(n):
    if n==1:
        return 1
    else:
        b=n//2
        return 1+binary(b)

m=100
print("The number of digits of ",m," in binary form: ",binary(100))