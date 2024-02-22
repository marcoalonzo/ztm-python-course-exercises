# Exercise Tricky Counter
# Write a program to find the sum of items in the list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Answer:
counter = 0
for item in my_list:
    counter = counter + item
    #can also use counter += item
print(counter)