arr=[2,5,1,4,3]
arr.sort()
# print(arr)
minsum=0
for i in range(len(arr)-1):
    minsum=minsum+arr[i]
maxsum=0
for i in range(1,len(arr)):
    maxsum=maxsum+arr[i]

print(minsum,maxsum)




