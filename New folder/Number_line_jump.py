# 0 3 4 2
# 0 2 5 3
# 21 6 47 3
# 4523 8092 9419 8076
x1=4523
v1=8092
x2=9419
v2=8076
def kangaroo(x1, v1, x2, v2):
    if x2>x1 and v2>v1:
        return 'NO'
    elif x2<x1 and v2<v1:
        return 'NO'
    else:
        sum1=x1
        sum2=x2
        while True:
            sum1=sum1+v1
            sum2 = sum2+v2
            if sum1==sum2:
                return 'YES'
                # break
            if sum1>=100000000 or sum2>=100000000:

                return 'NO'
                # break
