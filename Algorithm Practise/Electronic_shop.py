# keyboards=[40,50,60]
# drives=[5,8,12]
# b=60
# keyboards=[3, 1]
# drives=[5, 2, 8]
# b=10
keyboards=[4]
drives=[5]
b=5
count =0
for i in keyboards:
    for j in drives:
        if i+j<=b and (i+j)>=count:
            count=(i+j)

if count>0:
    print(count)
else:
    print(-1)