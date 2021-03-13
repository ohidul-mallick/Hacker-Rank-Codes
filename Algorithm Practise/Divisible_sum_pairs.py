# ar=[1,2,3,4,5,6]
ar=[1, 3, 2, 6, 1, 2]
# n=6
# k=5
n=6
k=3
pair=0
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        else:
            if (ar[i]+ar[j])%k==0:
                pair+=1

res=int(pair/2)
print(res)