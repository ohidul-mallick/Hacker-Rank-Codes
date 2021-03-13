def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)

def findlcm(a,b):
    if b==1:
        return a
    a=(a*b)//hcf(a,b)
    b-=1
    return findlcm(a,b)

n=int(input())
if n<3:
    print(n)
else:
    print(findlcm(n,n-1))