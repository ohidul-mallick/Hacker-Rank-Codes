arr=[4,4,1,3]
maxInt=0
maxCount=0
# minInt=0
for i in range(len(arr)):
    if maxInt<arr[i]:
        maxInt=arr[i]
    # elif minInt>arr[i]:
    #     minInt=arr[i]
for i in range(len(arr)):
    if maxInt==arr[i]:
        maxCount+=1

print(maxInt)
print(maxCount)