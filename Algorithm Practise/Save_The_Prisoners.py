
# m=2
# n=5
# s=2

m=2
n=5
s=1
# m=6
# n=4
# s=2
count=0
temp=m
# while(temp>=0):
#     for i in range(s,n+1):
#         temp-=1
#         count=i
#         print(temp)
#         if temp==0:
#             break
#     s=1
# print(count)

print((s+(m%n)-1)%n if((s+(m%n)-1)%n!=0) else n )


# result = (m - n * (m//n) + (s - 1))%n
# return n if result == 0 else result

'''
temp=s+m-1
d=(temp//n)*n
res=temp-d
if(temp-d==0):
    res=n
# return(res)
'''

'''
    x = (m+s-1) % n
    if x == 0: x = n
    return x
'''