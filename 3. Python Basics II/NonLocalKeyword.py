# Nonlocal Keyword

def outer():
    x = 'local' #local to the outer function

    def inner():
        nonlocal x #calls to use the x variable from the parent outer function. 
        #without the "nonlocal x", variable x would be a local variable to the inner function
        x = 'nonlocal' #assigning new string and replacing the value of the parent x variable
        print('inner:', x) #prints new string

    inner()
    '''
    sicne we've modified the value of x in the inner function, it will print the new
    value as well
    '''
    print('outer:', x)

outer()