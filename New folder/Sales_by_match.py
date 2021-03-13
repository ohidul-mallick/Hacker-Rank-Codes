# n=7
# ar=[1,2,1,2,1,3,2]
n=9
ar=[10 ,20, 20, 10, 10, 30, 50, 10, 20]
counts={}
for i in range(n):

    counts[ar[i]]=counts.get(ar[i],0)+1
# print(counts)
Sum=0
for key,value in counts.items():
    if value>1:
        r=value//2
        Sum=Sum+r
print(Sum)
