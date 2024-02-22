# Global Keyword

total = 0 #global scope


def count():
    '''
    global keyword allows us to use the global variable total
    '''
    global total 
    total += 1
    return total

'''
With the use of global keyword, we can use the global variable
'total' inside the function count() multiple times
'''
count()
count()
print(count())

#1 - start with local
#2 - parent local?
#3 - global
#4 - built in python functions