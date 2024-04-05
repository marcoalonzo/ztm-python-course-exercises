#Set and Dictionary Comprehensions

#creates set with characters in 'hello'
my_list = {char for char in 'hello'}
#creates set with number range 0-99
my_list2 = {num for num in range(0,100)}
#creates list with number range 0-99 multiplied by 2
my_list3 = [num * 2 for num in range(0,100)]
#creates set with number range 0-99 to the power of 2, but only displays even numbers
#added conditional to only include even numbers on list based on True/False condition
my_list4 = {num ** 2 for num in range(0,100) if num %2 == 0}

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

simple_dict = {
    'a': 1,
    'b': 2

}

#creates a dicionary with a power of 2 to the value of each key:value pair
#added condition to only add even numbers to the dictionary
my_dict = {k:v**2 for k,v in simple_dict.items() if v % 2 == 0}
#creates a dictionary where the item is the key and item multipled by two is the value
my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict)
print(my_dict2)

