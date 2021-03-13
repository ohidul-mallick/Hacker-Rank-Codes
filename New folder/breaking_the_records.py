# n=9
# score = [10, 5 ,20, 20, 4, 5, 2, 25, 1]

n=10
score=[3, 4, 21, 36 ,10, 28 ,35 ,5 ,24, 42]

Max=score[0]
Min=score[0]
maxCount = 0
minCount = 0
for i in range(1,n):
    # print(score[i])
    if Max<score[i]:
        Max = score[i]
        maxCount+=1
    if Min>score[i]:
        Min=score[i]
        minCount+=1
print(maxCount,minCount)