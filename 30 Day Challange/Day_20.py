
n=3
a=[3,2,1]
numberOfSwaps = 0
for i in range(n):
    
    for j in range(n-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1]=a[j+1],a[j]
            numberOfSwaps+=1
            print(numberOfSwaps)
    if numberOfSwaps==0:
        break

print(f'Array is sorted in {numberOfSwaps} swaps.')
a.sort
print('First Element:',a[0])       
print('Last Element:',a[n-1])