#Maggie Mulhall
#Find the average of an array of numbers
#Rounds to 2 decimals

#Input: Array and length of Array
#Output: Array's average
def mean(A,n):
    if n==1:
        return(A[0])
    else: 
        mini_mean=mean(A,n-1)
        return ((n-1)*mini_mean+A[n-1])/n

A=[-1.7, 6.5, 8.2, 0.0, 4.7, 6.3, 9.5, 12.2, 37.9, 53.2]
mean=mean(A,10)
print(round(mean,2))
    