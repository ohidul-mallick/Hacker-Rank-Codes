n=int(input())
num=n-1
s3=((num//3)+1)*((num//3)*3)//2

s5=((num//5)+1)*((num//5)*5)//2

s15=((num//15)+1)*(((num//15))*15)//2

Sum=s3+s5-s15
print(Sum)