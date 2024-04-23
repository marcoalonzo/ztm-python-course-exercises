#Decorators
def hello(func): #we pass in a function
    func() #we call the function we passed in

def greet():
    print ('still here')

a = hello(greet) #we pass in the greet function into the hello function
print(a)

# this example shows us that functions can also be used as variables.




