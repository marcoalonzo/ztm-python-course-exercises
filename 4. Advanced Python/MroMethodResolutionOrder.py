#MRO - Method Resolution Order

'''
class A:
    num = 10

class B(A): #B inherits from A and does nothing
    pass

class C(A): #C inherits from A and has the same variable as A
    num = 1

class D(B, C): # D inherits from both B and C, and does nothing
    pass

print(D.num) # MRO -> D -> B -> C -> A
print(D.mro()) #displays MRO of class D
'''

class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B,A,Z):
    pass

print(M.mro()) #displays MRO of class M
print(M.__mro__) #MRO dunder, displays the same info as its function
