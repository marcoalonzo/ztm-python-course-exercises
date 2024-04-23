#Higher Order Function (HOC)
#greet accepts a function
def greet(func):
    func()

#greet2 returns a function
def greet2():
    def func():
        return 5
    return func

print(greet(greet2))