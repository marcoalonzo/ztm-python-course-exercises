#iterable
#generators

# here we are generating our own generator function, just like a range().

'''
'yield' pauses the function and comes back to it when we do something to it, which is called 'next'.

if there is the keyword 'yield' written inside the function, then python recognises that its a 
generator function, and won't run the function until the function is being iterated.
'''

def generator_function(num):
    for i in range(num):
        yield i * 2 #pauses the function and comes back to it when something else is done to it

g = generator_function(100)
next(g) #keyword next tells the function to start back up and move onto the next item in the iterable
next(g)
print(next(g))
print(g) #printing the variable without next will give out the generator object

#for item in generator_function(1000):
 #   print(item)

#def make_list(num):
#    result = []
#    for i in range(num):
#        result.append(i * 2)
#    return result

#my_list = make_list(100)
#print(list(range(100000)))


