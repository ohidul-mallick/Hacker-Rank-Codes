n=5
a=[[1 ,2 ,100],[2, 5, 100],[3, 4, 100]]

lst=[]
for i in range(n):
    lst.append(0)


for i in a:
    print(lst)
    
    for j in range(i[0],(i[1]+1)):
        lst[j]=lst[j]+i[2]

print(lst)