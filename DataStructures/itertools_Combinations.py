from itertools import combinations
word, size= input().split()
letter=[w for w in word]

for i in range(1,int(size)+1):
    arr=[]
    for item in combinations(letter,i):
         arr.append("".join(sorted(item)))
         
    
    print("\n".join(sorted(arr)))