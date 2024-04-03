from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_names(item):
    return item.upper()

print(list(map(capitalize_names, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def high_scores(item):
    return item > 50

print(list(filter(high_scores, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
all_numbers = my_numbers + scores
#print(all_numbers)

def accumulator(acc, item):
    #print(acc, item)
    return acc + item

print(reduce(accumulator, all_numbers, 0))
'''
Another way to complete this instead of creating a new list:
print(reduce(accumulator, (my_numbers + scores)))
'''
    
