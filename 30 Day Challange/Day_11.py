res = []
arr=[
[1, 1, 1, 0, 0, 0],
[0 ,1 ,0 ,0 ,0 ,0],
[1, 1, 1, 0, 0, 0,],
[0 ,0 ,2 ,4 ,4 ,0],
[0 ,0 ,0 ,2 ,0 ,0],
[0 ,0 ,1 ,2 ,4 ,0]
]
# for row in range(4):
#     for column in range(4):
#         m = -100000
#     total = sum(arr[row][column:column+3]) + arr[row+1][column+1] + sum(arr[row+2][column:column+3])  

#     if total > m: m = total
#     res.append(m)


maxValue = -9 * 7

for i in range(len(arr) - 2):
    for j in range(len(arr[0]) - 2):
        maxValue = max(maxValue, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

print(maxValue)
