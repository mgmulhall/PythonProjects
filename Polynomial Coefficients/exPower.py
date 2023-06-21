#Maggie Mulhal;
# This program evaluates a polynomial of coefficients within in array and x val

# Input: number (X) and power (p)
# Output: value of x^p
def power(x, p):
    if p == 0:
        return 1
    result = x
    for i in range(p-1):
        result *= x
    return result

#print("power: ",power(7.7,3))

# Input: Array of coefficients (A) and value x
# Output: Evaluated polynomial of coefficients within in array and x val
A=[12.3,40.7,-9.1,7.7,6.4,0,8.9]
def evaluate(A,x):
    n = len(A)
    result = 0
    for i in range(n):
        temp=A[i] * (power(x,i))
        result = result+ temp
    return result

print(evaluate(A,5.4))