import math
# n=5
n=3

k=5
Sum=0
for day in range(n):
    like=math.floor(k/2)
    share=like*3
    k=share
    Sum=Sum+like
print(Sum)