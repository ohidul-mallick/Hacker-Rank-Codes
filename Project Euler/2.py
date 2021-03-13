n=int(input())
lst=[]

fibonacciFirst=1
fibonacciSecond = 2
fibonacciResult=1
for _ in range (n-2):
    fibonacciResult = fibonacciFirst + fibonacciSecond
    fibonacciFirst = fibonacciSecond
    fibonacciSecond = fibonacciResult
    if fibonacciResult>=n:
        break
    if fibonacciResult%2==0:
        lst.append(fibonacciResult)

print(sum(lst)+2)
