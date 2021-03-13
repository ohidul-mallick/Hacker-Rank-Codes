# n=15
# c=3

# m=2
n = 77232
c = 654
m = 40458

initialChocolate = n//c
Sum=initialChocolate
wLeft=initialChocolate

while(wLeft>0):
    w=initialChocolate
    if w>=m:
        cfw=w//m
        wLeft=initialChocolate%m
        Sum=Sum+cfw
        initialChocolate=wLeft+cfw
    else:
        break

print(Sum)