a=[1,1,2,2,4,4,5,5,5]
# a=[1 ,2 ,2, 3, 1, 2]
# a=[4 ,6 ,5 ,3 ,3 ,1]
n=len(a)

greaterMax=0
lesserMax=0
for i in range(n):
    greaterCount=0
    lesserCount=0
    for j in range(n):
        if a[i]>=a[j]:
            if abs(a[i]-a[j])<=1:
                greaterCount+=1
                if greaterMax<greaterCount:
                    greaterMax=greaterCount


        if a[i]<=a[j]:
            if abs(a[i]-a[j])<=1:
                lesserCount+=1
                
                if lesserMax<lesserCount:
                    lesserMax=lesserCount

if greaterMax>lesserMax:
    print(greaterMax)
else:
    print(lesserMax)

