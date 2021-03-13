# apples=[2,3,-4]
# oranges=[3,-2,-4]
# s=7
# t=10
# a=4
# b=12
apples=[-2 ,2 ,1]
oranges=[5 ,-6]
s=7
t=11
a=5
b=15
m=len(apples)
n=len(oranges)
appleCount=0
orangeCount=0
for i in range(m):
    if (a+apples[i])>=s and (a+apples[i])<=t:
        appleCount+=1
        
        
for j in range(n):
    if (b+oranges[j])>=s and (b+oranges[j])<=t:
        orangeCount+=1

print(appleCount)
print(orangeCount)

        