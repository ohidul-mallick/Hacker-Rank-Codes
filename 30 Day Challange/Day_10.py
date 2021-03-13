'''
Sample Input 1: 5
Sample Output 1: 1
Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .


Sample Input 2: 13
Sample Output 2: 2
Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is .
'''
a="{0:b}".format(125)
print('Original',a)
count=0
d=[]
m=0
for i in a:
    if i=='1':
        count+=1
        if count>m:
            m=count
    else:
        d.append(count)
        count=0
print(m)