a=[17,28,30]
b=[99,16,8]
count_a=0
count_b=0


for val,key in zip(a ,b):
    # print(val,key)
    if val>key:
        count_a+=1
    elif val<key:
        count_b+=1
    else:
        pass

print(count_a,count_b)