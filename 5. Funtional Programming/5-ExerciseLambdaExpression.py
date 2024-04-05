# Write a lambda expression that squares the values in my_list
my_list = [5, 4, 3]

print(list(map(lambda item: item*item, my_list)))

# Write a lambda expression to sort list based on the second value of each tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]


'''
We have to give sort a key and we want it to be the second value of each tuple [1].
We want to run the sort function on the list and the key for the sort function when 
we're sorting through everything is we want it to iterate over each item that we're 
we're going to get. That is, x is going to be a particular tuple, and and we want it 
to use the value which we're going to return, which is the second one. The key is 
always going to be by the second item.
'''
a.sort(key = lambda x: x[1])
print(a)

