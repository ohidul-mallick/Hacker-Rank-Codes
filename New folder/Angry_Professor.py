a=[0 ,-1 ,2 ,1]
k=2
# a=[-1, -3, 4, 2]
# k=3
# a=[-2,-1,0,1,2]
# k=3

Sum=0
for element in a:
    if element<=0:
        Sum+=1
if Sum>=k:
    print('NO')
else:
    print('YES')