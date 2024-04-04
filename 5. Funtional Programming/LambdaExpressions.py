#Lambda Expressions

from functools import reduce

my_list = [1,2,3]

'''
with lamba, since this function is only needed once, 
we don't need to define it

#def multiply_by2(item):
    #return item*2

#no longer needed as we've defined lambda expression below
#def only_odd(item):
    #return item % 2 != 0


function also not needed after lambda expression defined below
def accumulator(acc, item):
    print(acc,item)
    return acc + item

multiply_by2 and only_odd are "defined" and done within the lambda call,
which is a one time anonymous function that doesn't have defined name
'''
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 !=0 , my_list)))
print(reduce(lambda acc, item: acc + item, my_list))
print(my_list)


