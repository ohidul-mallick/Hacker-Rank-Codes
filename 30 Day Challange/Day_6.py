T=int(input())

for j in range(T):
    S=input()
    for i in range(len(S)):
        if i%2==0:
            print(S[i],end='')
    print(' ',end='')
    for i in range(len(S)):
        if i%2!=0:

            print(S[i],end='')
    print()