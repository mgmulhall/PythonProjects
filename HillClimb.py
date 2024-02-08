"""
This Python script implements the Hill Climbing algorithm to find the local maximum value in an array.

The `hillClimb` function takes an array and a starting index as input and returns the index and value of the local maximum found.
The `myFunction` function generates an array based on certain conditions, which can be replaced with any other function as per requirement.
The `main` function demonstrates the usage of the `hillClimb` function by generating an array using `myFunction`, finding a random starting index, and then finding the local maximum using the Hill Climbing algorithm.

"""


import random
from math import *

def myFunction(x):
    #given function to generate array
    if x == 0:
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x))**3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2)**3
    else:
        return (log2(x)**2) - x

def hillClimb(arr, start_index):
    #Initializations
    n = len(arr)
    current_index_r=None
    current_index_l=None
    
    # Function to check if an index is a peak
    def is_peak(index):
        if index == 0: #if first
            return arr[index] >= arr[index + 1]
        elif index == n - 1: #if last
            return arr[index] >= arr[index - 1]
        else:
            return arr[index] >= arr[index - 1] and arr[index] >= arr[index + 1]

    # Function to check if an index is in a pitt
    #   Return True if starting is in a pitt, otherwise False
    #   Return "R" or "L" to determine which direction to search next (Left or Right)
    def is_pit(index):
        if index==0: #if first
            if arr[index] <= arr[index + 1]:
                return "True","R"
            else:
                return "False","n/a"
        elif index == n - 1: #if last
            if arr[index] <= arr[index - 1]:
                return "True","L"
        
        #if pit, determine which direction to move
        elif arr[index] <= arr[index - 1] and arr[index] <= arr[index + 1]:
            #is pitt
            if arr[index - 1] > arr[index + 1]:
                #left is bigger, return L
                return "True","L"
            else:
                #return R if right is bigger or if left=right
                return "True","R"
        else:
            #not a pitt, return false
            return "False","n/a"
            
    #Function to search from current index moving right
    def search_right():
        current_index_r=start_index
        while (current_index_r + 1) < n and arr[current_index_r+1] >= arr[current_index_r]:
            current_index_r += 1
        return current_index_r

    #Function to search from current index moving left
    def search_left():
        current_index_l = start_index
        while (current_index_l -1) >= 0 and arr[current_index_l-1] >= arr[current_index_l]:
            current_index_l -= 1
        return current_index_l
    
    # Check if the starting index is a peak
    if is_peak(start_index):
        return start_index, arr[start_index]
    
    #If starting is in a pitt, determine which direction to move and move
    is_pitt,direction=is_pit(start_index)
    if is_pitt=="True":
        if direction=="L":
            current_index_l=search_left()
        else:
            current_index_r=search_right()
    if current_index_r!=None:
        return current_index_r,arr[current_index_r]
    elif current_index_l!=None:
        return current_index_l,arr[current_index_l]
    else:
        current_index_r=search_right()
        current_index_l=search_left()

    # Return the local maximum index and value
    if current_index_r == n:
        return current_index_l, arr[current_index_l]
    elif current_index_l < 0 or arr[current_index_l] >= arr[current_index_r]:
         return current_index_l, arr[current_index_l]
    else:
        return current_index_r, arr[current_index_r]

def main():
    #Create array with myFunction
    x_values=[]
    for i in range(9999):
        x_values.append(i)
    y_values=[]
    for x in x_values:
        y_values.append(myFunction(x))

    #Generate random starting index
    start_index=random.randint(0,9998)
    
    #Assign y_values to arr
    arr=y_values
    
    # Find the local maximum of the array with hillClimb
    local_maximum_index, local_maximum_value = hillClimb(arr, start_index)

    # Print the local maximum index and value
    print("Local maximum index:", local_maximum_index)
    print("Local maximum value:", local_maximum_value)

main()