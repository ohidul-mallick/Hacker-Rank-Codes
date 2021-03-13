a=[1 ,2 ,3]
k=2
# quaries=[0,1,2]
quaries=2
# a=[3,4,5]
# k=2
# quaries=[1,2]
for i in range(k):
    n=a.pop()
    a.insert(0,n)
# for j in quaries:
print(a[quaries])