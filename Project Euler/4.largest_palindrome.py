n=800000
lst=[]
for i in range(100,1000):
    for j in range(100,1000):
        a=i*j
        if str(a)==str(a)[::-1] and a not in lst:
            lst.append(a)
lst.sort()
length=len(lst)
for i in range(length-1,-1,-1):
    if lst[i]<n:
        print(lst[i])
        break


