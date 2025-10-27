dict1 = {'a': 1 , 'b':2}
dict2 = {'b':1, 'c':3}

dict3= dict1.copy()
dict3.update(dict2)

print(dict1)
print(dict2)
print(dict3)