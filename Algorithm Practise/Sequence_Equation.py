p=[5,2,1,3,4]
res=[]
for i in range(1,len(p)+1):
    a=p.index(i)
    res.append(p.index(a+1)+1)
print(res)
