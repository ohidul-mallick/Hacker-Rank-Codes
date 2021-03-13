def count_substring(string, sub_string):
    flag=True
    count=1
    s=0
    while flag:
        a=string.find(sub_string,s)
        if a==-1:
            flag=False
        else:
            s=a+1
            count+=1
    return count
