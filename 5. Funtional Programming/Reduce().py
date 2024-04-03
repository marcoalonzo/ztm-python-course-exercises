#Reduce
from functools import reduce

my_list = [1,2,3]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item): #accumulator defaults to 0, if non is given
    print(acc,item)
    return acc + item

#reduce requires 3 paramaters (function, data, initial value)
print(reduce(accumulator, my_list, 10))
print(my_list)


