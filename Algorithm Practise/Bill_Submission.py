bill=[3, 10, 2, 9]
k=1
n=4
# b=12
b=7
n=len(bill)
Sum=0
for i in range(n):
    if i==k:
        continue
    else:
        Sum=Sum+bill[i]
# print(Sum)
bActual=int(Sum/2)
if bActual==b:
    print('Bon Appetit')
else:
    print(b-bActual)
