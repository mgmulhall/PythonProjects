#Maggie Mulhall
#The program produces the sum of squares of an integer

#Input: Integer
#Output: Sum of squares up to inputted integer
def sos(n):
    k=0
    if n==1:
        return 1
    else:
        b=n-1
        return((n**2)+sos(b))
a=5
print("The some of the squares of ",a," is ",sos(a))