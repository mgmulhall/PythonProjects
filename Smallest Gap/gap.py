#Maggie Mulhall
#This program finds the smallest gap between instances in an array

#Input: Array of real numbers
#Output: Integer representing the smallest gap between elements in the array
def gap(array):
    #Save length of array
    n = len(array)
    #Initialize empty float
    result = float('inf')
    #Loop through array & find smallest difference using absolute value
    for i in range(n):
        for j in range(i+1, n):
                temp=abs(array[i]-array[j])
                #print("temp:",temp)
                if temp<result:
                    result=temp
    return result

#Main block to initialize array, call function and print results
def main():
    array=[12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
    print(gap(array))
main()