# a=[7, 1, 3, 4, 1, 7]
a=[1,2,3,4,5]
# a=[3,2,1,2,3]
lst=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            lst.append(abs(j-i))
if len(lst)>0:
    print(min(lst))
else:
    print(-1)