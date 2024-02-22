# Exercise Functions
# Highest Even: Write a function to find the highest even number from the following list: [10,2,3,4,8,11].

#Answer:

def highest_even(list):
  even_numbers = []
  for numbers in list:
    #if a number is even, we'll append it to the even_numbers list
    if numbers % 2 == 0:
      even_numbers.append(numbers)
  return max(even_numbers) #max is a built-in function that gives us the max number in a list
  
print(highest_even([10,2,3,4,8,11]))
