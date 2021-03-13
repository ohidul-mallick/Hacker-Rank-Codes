

# h=[1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
# word='torn'
# h=[1 ,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# word='abc'

h=[1 ,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word='zaba'


Max=0
def convert(alph):
    a=alph.lower()
    num=ord(a)-97
    return num

for w in word:
    num=convert(w)
    if h[num]>Max:
        Max=h[num]

res=Max*1*len(word)

print(res)