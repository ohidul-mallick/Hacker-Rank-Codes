# str1='aabbccdde'
# str1='zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'


# dict1={}
# str2=''
# for x in str1:
#     dict1[x]=dict1.get(x,0)+1

# for key,value in dict1.items():
#     if value%2!=0:
#         str2=str2+key

# if len(str2)<1:
#     print('Empty String')
# else:
#     print(str2)

# print(dict1)


s ="aaabccddd"
while True:
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i]+s[i+2:]
            break
    else:
        break
print(s if s else "Empty String")


