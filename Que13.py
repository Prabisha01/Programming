# concatenate following dictionaries to create a new one.
dict1 = {1:'c', 2:'d'}
dict2 = {5:'v', 4:'e'}
dict3 = {6:'b', 7:'f'}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)