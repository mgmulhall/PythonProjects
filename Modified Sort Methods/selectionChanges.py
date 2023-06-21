#Maggie Mulhall
#This program is an adapted version of the selection sort method

# Input: An array A and indices i and j.
# Output: An array where A[i] and A[j] have been swapped.
def Swap(A, i, j):
 temp = A[i]
 A[i] = A[j]
 A[j] = temp

# Input: An array A of integers.
# Output: Array A sorted in increasing order.
# Displays the number of Comparisons, Swaps and the Array at each phase
def SelectionSort(A):
 for i in range(len(A)-1):
  comp=0
  swaps=0
  m = len(A) - 1 - i  
  
  #Loop and Compare
  for j in range(len(A)-i-1):
    comp+=1
    if A[j] > A[m]: 
           m = j

  #Make/Track Swaps
  Swap(A, len(A)-1-i, m) 
  swaps+=1

  #Display each step
  print("\n",A)
  print("Swaps: ",swaps)
  print("Comparisons: ",comp)
  
A=[99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
SelectionSort(A)