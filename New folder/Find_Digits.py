# n=12
# n=124
# n=111
# n=10
n=1012



count=0
for i in str(n):
    if i=='0':
        continue
    else:
        if n%int(i)==0:
            count+=1

print(count)