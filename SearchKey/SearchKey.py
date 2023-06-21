#Maggie Mulhall
#This program determines the location (index) of a number in an array

#Imports
import math

#Input:
#  Descending sorted array
#  Left(lowest index) 
#  Right(highest index) 
#  Search key
#Output:
    #Index of search key on array
def descending_binary_search(array,left,right,searchkey):
    mid_index=math.floor((right+left)//2)
    if left>right:
        return None
    elif array[mid_index] == searchkey:
        return mid_index
    elif array[mid_index] < searchkey:
        return descending_binary_search(array,left,mid_index-1, searchkey)
    elif array[mid_index] > searchkey:
        return descending_binary_search(array,mid_index+1, right, searchkey)

array=[100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18]
left=0
right=14
searchkey=40
print(descending_binary_search(array,left,right,searchkey))