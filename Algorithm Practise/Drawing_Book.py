# n=6
# p=2
# n=5
# p=4
# n=5
# p=1
# n=7
# p=4
n=37455

p=29835
i=1
Sum=0

if p==n/2 or p==1:
    Sum=0

elif p<=n/2:
    while(i<=p):
        Sum+=1
        i+=2
else:
    if n%2!=0 and n-p==1:
        Sum=0
    else:
        temp=n
        while(temp>p):
            Sum+=1
            temp -=2
        if temp%2!=0 and p%2==0:
            Sum=Sum-1

print(Sum)
