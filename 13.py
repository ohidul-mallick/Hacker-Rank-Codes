
password='0#)+g!'


length=len(password)

upper=0
lower=0
digit=0
special=0
req=0
res=0
special_char="!@#$%^&*()-+?_=,<>/"
for i in range(length):
    if password[i]>='A' and password[i]<='Z':
        upper+=1
    if password[i]>='a' and password[i]<='z':
        lower+=1
    if password[i]>='0' and password[i]<='9':
        digit+=1
    if password[i] in special_char: 
        special+=1

print(special)
print(digit)
print(lower)
print(upper)

if upper==0:
    req+=1
if lower==0:
    req+=1
if digit==0:
    req+=1
if special==0:
    req+=1

if length<=6:
    res=6-length

if res>=req:
    print("result :",res)
else:
    print("Required :",req)



