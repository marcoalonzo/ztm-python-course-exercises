# Exercise Type Conversion
# Write a program which tells your age

birth_year = input('What year were you born?\n') #input will come in as a string
age = 2023 - int(birth_year) #we have to convert the string variable birth_year into an integer
print(f'Your age is {age} years.') #we use formatting string to add variable age into the printed output