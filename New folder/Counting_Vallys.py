# paths='DDUUUUDD'
paths='UDDDUDUU'
# paths='DDUUDDUDUUUD'
steps=8
# steps=12
count=0
Max=0

for i in range(steps):
    if paths[i]=='D':
        count-=1
    else:
        count+=1
    # if count>0 and count>Max:
    #     Max=count
    if count==0 and paths[i]=='U':
        Max+=1

print(Max)
