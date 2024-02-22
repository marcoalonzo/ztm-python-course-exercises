# *args and **kwargs

'''
*args allows us to grab any number of positional arguments
**kwargs allos us to grab any number of keywword agurments and get a dictionary
'''
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    #obtain the values of the dictionary
    for item in kwargs.values():
        total += item #count total number of items
    print(i, name)
    #total sum of the positional arguments sum plus dict value sum
    return sum(args) + total 


print(super_func('wisntone', 1, 2, 3, 4, 5, i='hello', num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs