s='oneTwoThree'
count=0
ind=0
for i in range(len(s)-1):

    if s[i]>='A' and s[i]<='Z':
        count+=1
        print(s[ind:i])
        ind=i
print(s[ind:])
print(count+1)
