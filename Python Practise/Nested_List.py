lst=[]
fList=[]
valuList=[]

for _ in range(int(input())):

    name = input()
    score = float(input())
    lst.append([name,score])
    valuList.append(score)

valuList.sort()
sLow=valuList[1]

for name,value in lst:
    if value==sLow:
        fList.append(name)

for name in sorted(fList):
    print(name)
    

