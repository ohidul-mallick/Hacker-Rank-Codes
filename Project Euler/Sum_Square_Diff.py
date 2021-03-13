import math
n=int(input())

def squaresum(n): 
    return (n * (n + 1) / 2) * (2 * n + 1) / 3
def sumSq(n):
    return n*(n+1)//2

Sum=squaresum(n)
Sum1=sumSq(n)

a=Sum1*Sum1
print(int(a-Sum))

