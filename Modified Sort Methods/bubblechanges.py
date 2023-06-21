#Maggie Mulhall
#This program is an adapted version of the bubble sort method

# Input: An array A of integers.
# Output: An array A sorted in increasing order.
def bubble_sort(A):
    n = len(A)
    all_comp = 0  
    all_swap = 0  
    for k in range(n-1):
        comps = 0  
        swaps = 0  
        for i in range(n-k-1):
            if A[i] > A[i+1]:
                Swap(A, i, i+1)
                swaps += 1
            comps += 1
        all_comp += comps
        all_swap += swaps

        #Display each step
        print("\nIteration: ",k+1," ",A)
        print("Comparisons: ",comps)
        print("Swaps: ",swaps)
        if swaps == 0:
            print("Exit at iteration", k+1)
            break
    print(f"Total Comparisons: {all_comp}, Total Swaps: {all_swap}")

# Input: An array A and indices i and j.
# Output: An array where A[i] and A[j] have been swapped.
def Swap(A, i, j):
 temp = A[i]
 A[i] = A[j]
 A[j] = temp

A=[6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
bubble_sort(A)