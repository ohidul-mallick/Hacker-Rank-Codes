n = int(input('Enter : '))
# prime_numbers = [2,3]
# i=3
# if(0<n<3):
#     print(prime_numbers[n-1])
# elif(n>2):
#     while (True):
#         i+=1
#         status = True
#         for j in range(2,int(i/2)+1):
#             if(i%j==0):
#                 status = False
#                 break
#         if(status==True):
#             prime_numbers.append(i)
#         if(len(prime_numbers)==n):
#             break
#     print(prime_numbers[n-1])

i=3
count=2

while True:
    i+=1
    status=True
    for j in range(2,int(i/2)+1):
        if i%j==0:
            status=False
            break
    if status==True:
        count+=1
    if count==n:
        print(i)
        break

