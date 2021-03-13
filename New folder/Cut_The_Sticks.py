# arr=[1,2,3]
arr=[8 ,8 ,14 ,10 ,3 ,5 ,14 ,12]
# arr=[1 ,2 ,3 ,4 ,3 ,3 ,2 ,1]
# arr=[5 ,4 ,4 ,2 ,2 ,8]
res=[]
while len(arr)>1:
    arr=[i for i in arr if i!=0]
    if len(arr)<1:
        break
    res.append(len(arr))
    m=min(arr)
    arr=[x-m for x in arr]
print(res)

