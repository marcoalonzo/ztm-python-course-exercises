# While loops

i = 0
'''
while i is less than 50, print i, then add 1 to i.
Loop repeats until i is 50
'''
while i < 50:
    print(i, end='\t')
    i += 1
else:
    #Once i is >= 50, print the statement
    print('\nDone with all the work.')
print()


my_list = [1, 2, 3]
i = 0
'''
Loops through the list until i is greater than
the length of the list
'''
while i < len(my_list):
    print(my_list[i])
    i += 1
print()

while True:
    response = input('Say Something: ')
    if response == 'bye':
        break