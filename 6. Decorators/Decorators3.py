#Decorator

#this decorator is going to accept a function
def my_decorator(func):
    def wrap_func(*args, **kwargs): #passed in parameters from the hello function
        print('********') #adding extra functionality to the called function
        func(*args, **kwargs) #parameters from the hello function
        print('********') #adding extra functionality to the called function
    return wrap_func

#hello function is wrapped into my_decorator function
@my_decorator
def hello(greeting, emoji = ':('): #pass in an argument that's now required in my_decorator's wrap function in order to work
    print(greeting, emoji)

hello('hi!') #parameter is now required





