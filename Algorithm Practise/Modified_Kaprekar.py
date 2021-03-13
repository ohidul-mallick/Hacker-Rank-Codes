p=400
q=700
c=0
for i in range(p,q+1):

    a=i*i


    l=len(str(a))
    if l%2==0:
        n=str(a)
    else:
        n='0'+str(a)

    a=len(n)
    h=a//2
    w1=n[:h]
    w2=n[h:]
    w=int(w1)+int(w2)
    if w==i:
        c+=1
        print(i)
if c==0:
    print('INVALID RANGE')


