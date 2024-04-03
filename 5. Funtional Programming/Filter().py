#Filter()

my_list = [1,2,3]
def multiply_by2(item):
    return item*2

#filter() is going to try and receive a true and false value (bool) 
def only_odd(item):
    return item % 2 != 0 #if remainder isn't equal 0, it gets added to the new list it creates

print(list(filter(only_odd, my_list)))
print(my_list)


