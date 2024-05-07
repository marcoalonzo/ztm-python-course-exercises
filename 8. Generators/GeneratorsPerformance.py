#Generators
#We're creating a performance to measure how fast our code runs

#generators are much more performant than lists. (i.e range > list in performance.)

#So generators are really, really useful when calculating large sets of data.

from time import time #importing time object/module that we get from Python

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time() #checks time at start of function
        result = fn(*args, **kwargs)
        t2 = time() #checks time at end of function
        print(f'took {t2-t1} s') #calculate how much time it took for the function to finish running
        return result
    return wrapper
    
@performance
def long_time():
    print('1')
    for i in range(100000000): #range generator
        i * 5

@performance
def long_time2():
    print('2')
    for i in list(range(100000000)): #creates list in memory
        i * 5

long_time()
long_time2()


