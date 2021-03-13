arr=[1,2,2,3]
# arr=[3, 3, 2, 1, 3]
d={}
Max=0
for element in arr:
    d[element]=d.get(element,0)+1

for value in d.values():
    if Max<value:
        Max=value
    

print(len(arr)-Max)
