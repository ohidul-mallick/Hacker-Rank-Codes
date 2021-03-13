
s=[1, 2, 1, 3 ,2]


d=3
m=2
count=0
for i in range(len(s)):
    j=0
    sum1=0
    x=m
    while x!=0:

        if (i+j)>len(s)-1:
            break
        sum1=sum1+s[i+j]

        j+=1
        x-=1


    if sum1==d:
        count+=1

print(count)


'''
Q_num : 3
d=18
m=7
s=[2 ,5 ,1 ,3 ,4 ,4 ,3 ,5 ,1 ,1 ,2 ,1 ,4 ,1 ,3 ,3 ,4 ,2 ,1]

Q_Num : 2
s=[1, 1, 1, 1, 1, 1]

d=3
m=2
'''