some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

'''
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
'''

#Create a comprehension list that returns the duplicates in some_list just like in our previous loop exercise (see above)
duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)


