dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']
lstDict=[sorted(i) for i in dictionary]
lstQ=[sorted(i) for i in query]
lst=[lstDict.count(w) for w in lstQ]
print(lst)





