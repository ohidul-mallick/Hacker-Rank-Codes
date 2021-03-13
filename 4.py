arr=[[1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

diag1=[]
diag2=[]
length=len(arr)
for i in range(length):
    diag1.append(arr[i][i])
    diag2.append(arr[i][length-1-i])
    
sum1=sum(diag1)
sum2=sum(diag2)
res=sum1-sum2
print(abs(res))