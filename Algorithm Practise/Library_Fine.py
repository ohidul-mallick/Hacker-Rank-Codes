# 9 6 2015
# 6 6 2015
# 2 7 1014
# 1 1 1015
import time
start_time = time.time()
d1=2
m1=7
y1=1014
d2=1
m2=1
y2=2015


if y1==y2:
    if m1==m2:
        days=abs(d1-d2)
        print(days*15)
    else:
        print(abs(m1-m2)*500)


print("Process finished --- %s seconds ---" % (time.time() - start_time))



if y1>y2:
    print((y1-y2)*10000)
elif m1>m2:
    print((m1-m2)*500)
elif d1>d2:
    print((d1-d2)*15)
else:
    print(0)