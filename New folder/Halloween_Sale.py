# p=16
# d=2
# m=1
# s=9981
# p=20
# d=3
# m=6
# s=85
# s=80
# s=70
# p=100
# d=1
# m=1
# s=99
p=100
d=19
m=1
s=180
Sum=0
c=1
if p>s:
    print(0)
else:
    while (p>m and s>p):
        
        Sum=Sum+p
        print('sum ',Sum)
        s=s-p
        print('s ',s)
        c+=1
        p=p-d
        print('c ',c)
        print('p ',p)
    if p<=m:
        c=c-1
        while(s>=m):
            s=s-m
            c+=1
    print(c)
