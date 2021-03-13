# q=[1,2,3,5,4,6,7,8]
# q=[4,1,2,3]
q=[2, 1, 5, 3, 4]

# res2=[1,2,3,4,5]
n=len(q)
res=[]
newQ=q.copy()
newQ.sort()
count=0
for i in range(n):
    if q[i]!=newQ[i]:
        if q[i]==newQ[i+1]:
            count+=1
            newQ[i],newQ[i+1]=newQ[i+1],newQ[i]
        elif q[i]==newQ[i+2]:
            count+=2
            newQ[i],newQ[i+1],newQ[i+2]=newQ[i+2],newQ[i],newQ[i+1]

        else:
            print('Too chaotic')
            return

print(count)

if max(res)>2:
    print('Too chaotic')
else:
    print(int(sum(res)//2))





























'''


lst=[]
count=0
Min=q[0]
unsortedNum=0
unsortedPos=0
for i in range(n-1):
    if q[i]>q[i+1]:
        unsortedNum=q[i]
        unsortedPos=i

        for j in range(unsortedPos,n):
            if unsortedNum>q[j]:
                count+=1
        lst.append(count)


if max(lst)>2:
    print('Too chaotic')
else:
    print(count)
'''