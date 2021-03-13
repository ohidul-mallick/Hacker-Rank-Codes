i=20
j=23
k=6
Sum=0
def reverse(n):
    a=str(n)[::-1]
    return int(a)

# print(reverse(12))

for x in range(i,j+1):
    if (x-reverse(x))%k==0:
        Sum+=1
print(Sum)