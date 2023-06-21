#Maggie Mulhall
#This program does matrix multiplication
#Can be run with decimals and negative numbers

#Input:
# 1. N: Size of matrices
# 2. A: Matrix 1
# 3. B: Matrix 2

#Output:
# C: Product matrix

def matrix_multiplication(n, A, B):
    # Initialize empty matrix of size n
    C = [[0 for i in range(n)] for j in range(n)]
    # iterate over each row of matrix A
    for i in range(n):
        # iterate over each column of matrix B
        for j in range(n):
            # iterate over each element of the row i in matrix A and column j in matrix B
            for k in range(n):
                # update the value of the element in C at row i and column j
                C[i][j] += A[i][k] * B[k][j]
    return C

def main():
    # define the input matrices A and B
    A = [[1,0,2],[3,2,5],[6,2,3]]
    B = [[3,25,1],[4,8,0],[5,75,6]]
    n=3
    #Print the product of A and B
    print(matrix_multiplication(n, A, B))

main()
