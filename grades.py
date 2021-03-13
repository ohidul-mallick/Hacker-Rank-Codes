# n=4
grades = [73,67,38,33]
n=len(grades)
d=[]
def get_rem(a):
    if a>37:
        x=a%5
        if x<3:
            return a
        else:
            y=a//5
            z=(y+1)*5
            return z
    else:
        return a

for i in range(n):
    d.append(get_rem(grades[i])) 
print(d)

# # if  
# # for i in grades

# a=44



# print(get_rem(a))

