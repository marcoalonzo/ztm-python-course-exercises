#Decorator
#We're creating a performance to measure how fast our code runs
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
    for i in range(100000000):
        i * 5

long_time()


