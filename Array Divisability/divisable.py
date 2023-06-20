#Maggie Mulhall
#This Program determines the amount of instances in an array that are evenly divisible by a given number

#Input:
# 1. Array of real numbers
# 2. Integer 
#Output: 
# 1.Integer representing the amount of elements evenly divisible by the inputted integer

def divisible(array,int):
    count=0
    for i in array:
        if i%int==0:
            count+=1
    return count

#Initialize array and int, call function, print results
def main():
    array=[18, 54, 76, 81, 36, 48, 99]
    int=9
    print(divisible(array,int))
main()


