
arr=[1,0,1,-1,-1]
positive=0
negative=0
zeros=0
count=0
# Complete the plusMinus function below.

for element in arr:
    if element>0:
        positive+=1
    elif element<0:
        negative+=1
    elif element==0:
        zeros+=1
    count+=1
# print(float(positive)/float(count))
# print("{:.6f}".format(positive/count))
print('{:.6f}'.format(positive/count))