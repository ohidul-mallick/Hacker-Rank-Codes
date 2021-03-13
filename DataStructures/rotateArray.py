ar=[1,2,3,4,5,6]
lst=ar.copy()
for i in range(2):
    z=ar.pop(0)
    ar.append(z)
print(ar)
