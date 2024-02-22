# Scope Rules - what variables do I have access to?

a = 1 #global scope

def parent():
    a = 10 #function scope local to parent and child function (confusion)

    def confusion():
        a = 5 #function scope local to confusion
        return a
    return confusion()


print(a) #prints global scope variable
print(parent()) #prints value of parent function
