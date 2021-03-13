from itertools import permutations
s,k=map(str,input().split())
a=int(k)
z=list(permutations(s,a))
lst=[]
for i in z:
    b=''
    for j in range(a):
        b=b+i[j]
    lst.append(b)
lst.sort()
for i in lst:
    print(i)