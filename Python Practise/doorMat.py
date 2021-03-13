n=9
m=27
for i in range(n):
    for j in range(m):
        if j==int(m//2)+1:
            print('|',end='')
        if j==int(m//2) or j==int((m//2)+2):
            print('.',end='')
        else:
            print('-',end='')
    print()