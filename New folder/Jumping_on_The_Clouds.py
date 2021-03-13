# c=[0,1,0,0,0,1,0]
c=[0 ,0 ,0 ,1 ,0 ,0]
# c=[0 ,0, 1, 0, 0, 1, 0]
# c=[0 ,0 ,0 ,0 ,1 ,0]
# c=[0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0]
count=0
a=0

# while a<len(c)-1:
#     if 




def jumpingOnClouds(c):
    x=0
    y=0
    while(x!=len(c)-1):
        if(x+2<=len(c)-1 and c[x+2]==0):
            y+=1
            x=x+2
            
        else:
            y+=1
            x=x+1
    return y

print(jumpingOnClouds(c))