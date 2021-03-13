# height=[1,2,3,3,2]
# k=1
height=[2 ,5 ,4 ,5 ,2]
k=7
# height=[1, 6 ,3 ,5 ,2]
# k=4


m=max(height)

if k>=m:
    print(0)
else:
    print(m-k)