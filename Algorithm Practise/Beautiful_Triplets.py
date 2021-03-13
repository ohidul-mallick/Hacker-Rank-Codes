arr=[1 ,2 ,4 ,5, 7 ,8 ,10]
# arr=[2,2,3,4,5]
# d=1
d=3
count=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if j<=(len(arr)-2):
            print('arr[i] ',arr[i])
            print('arr[j] ',arr[j])
            print('arr[j+1] ',arr[j+1])
            
            if (arr[j]-arr[i])==d and (arr[j+1]-arr[j])==d:
                count+=1
                print('count ',count)

print(count)