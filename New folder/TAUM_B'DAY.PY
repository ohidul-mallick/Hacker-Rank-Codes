
# b=3
# w=5
# bc=3
# wc=4
# z=1
b = 10
w = 10
bc = 1
wc = 1
z = 1


lst=[]
c1=(b*bc+w*wc)
c2=((b*bc)+(w*bc)+(w*z))
c3=((w*wc)+(b*wc)+(b*z))
lst.append(c1)
lst.append(c2)
lst.append(c3)
print(min(lst))