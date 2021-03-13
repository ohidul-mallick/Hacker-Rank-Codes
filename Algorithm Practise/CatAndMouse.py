import math
# x=2
# y=5
# z=4
x=1
y=3
z=2
# x=1
# y=2
# z=3

CatADistance=abs(x-z)
CatBDistance=abs(y-z)
# print(CatADistance)
if CatADistance>CatBDistance:
    print('Cat B')
elif CatADistance<CatBDistance:
    print('Cat A')
else:
    print('Mouse C')
