n=3
import operator
topic=['10101','11110','00010']
d={}
x=[]
Max=0
count=0
for i in range(n-1):
    for j in range(len(topic[i])-1):
        a=topic[i]
        b=topic[i+1]
        if a[j]==1 or b[j]==1:
            # count+=1
    x.append(count)

for i in x:
    d[i]=d.get(i,0)+1

# res=max(d.items(), key=operator.itemgetter(1))[0]
# print(res)
for value in d.values():
    if value>Max:
        Max=value
for key,value in d.items():
    if value==Max:
        print(value,key)