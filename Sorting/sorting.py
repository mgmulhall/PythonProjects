#Maggie Mulhall
#This program compares the efficiency of the merge sort and the bubble sort

#Imports & initalizations
import random
from datetime import datetime
unsorted_list = []

#Create unsorted lists
for i in range(0,10000):
    n = random.randint(0,9)
    unsorted_list.append(n)
#print("unsorted: ",unsorted_list)
unsorted_list_copy=unsorted_list

#MERGE
def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
# Find the middle point to divide the list
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))
# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res

#BUBBLE
def bubble_sort(list):
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
               
#Get the current timestamp in milliseconds
def get_time():
   dt = datetime.now()
   time=(datetime.timestamp(dt)*1000)
   return time

#Main function
def main():
    print("\nTime is measured in milliseconds")
   
   #Preform merge
    #print("unsorted: ",unsorted_list)
    before_merge_time=get_time()
    sorted_list= merge_sort(unsorted_list)
    after_merge_time = get_time()
    #print("Merge sorted: ",sorted_list)
    merge_time=after_merge_time-before_merge_time
    print("Merge Time: ",(merge_time))
    
   
   #Preform bubble
    #print("unsorted copy: ",unsorted_list_copy)
    before_bubble_time = get_time()
    bubble_sort(unsorted_list_copy)
    after_bubble_time=get_time()
    bubble_sorted=unsorted_list_copy
    #print("Bubble sorted: ",bubble_sorted)
    bubble_time=after_bubble_time-before_bubble_time
    print("Bubble Time: ",(bubble_time))
    
    #Display difference
    print("Bubble took ",(bubble_time/merge_time)," times longer to sort 1000 numbers.")

#Call main function
if __name__ == "__main__":
   main()