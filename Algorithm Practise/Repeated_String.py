# s='abcac'
# s='ceebbcb'

s='gfcaaaecbg'
n=547602
temp=s
# n=10
# n=817723
# n=1000000000000
count=0
multiple=n//len(s)
rem=(n%len(s))

z=sum(x == 'a' for a in s for x in a)
y=sum(x == 'a' for a in s[:rem] for x in a)


res=z*multiple+y
print(res)
