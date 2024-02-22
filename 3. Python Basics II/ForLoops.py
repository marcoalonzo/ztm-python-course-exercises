# For Loops

for item in 'Zero to Mastery':
    #prints every item in the iterable, which is the string 'Zero to Mastery'
    print(item, end=' ') 
print()

for item in [1, 2, 3, 4, 5]:
    #prints every item in the iterable, which is the entirety of the list
    print(item, end=' ') 
print()

for item in {1, 2, 3, 4, 5}:
    #prints every item in the iterable, which is the entirety of the set
    print(item, end=' ')
print()

for item in (1, 2, 3, 4, 5):
    #prints every item in the iterable, which is the entirety of the tuple
    '''prints every item in the iterable, which is the entirety of the tuple,
    a total of 3 times until it moves to the next value, then repeats the process
    '''
    print(item, end=' ')
    print(item, end=' ')
    print(item,  end=' ')
print(item) #this is outside of the loop and will only print once
'''
printing "item outside of the loop will print out the value of the last "item" 
in the iteravble that was assigned to the variable "item". In this example the
value of the "item" right now is 5.
'''
print(item) 


# Nested Loops
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        '''
        #Processes everything in the second for loop with the first item value 
        from the initial loop first before it backouts back to the first for 
        loop to iterate over it agains with the second item value, so on and 
        so forth until it reaches the end of the first loop.
        '''
        print(item, x, end='\t')
        