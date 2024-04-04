#List comprehensions

#creates list with characters in 'hello'
my_list = [char for char in 'hello']
#creates list with number range 0-99
my_list2 = [num for num in range(0,100)]
#creates list with number range 0-99 multiplied by 2
my_list3 = [num * 2 for num in range(0,100)]
#creates list with number range 0-99 to the power of 2, but only displays even numbers
#added conditional to only include even numbers on list based on True/False condition
my_list4 = [num ** 2 for num in range(0,100) if num %2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

