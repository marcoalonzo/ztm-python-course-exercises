# Inheritance

#Class
class User():
    '''
    if we don't have variables or attributes that we want to assign to the user,
    we don't need to use the __init__ method when creating the class function
    '''
    def sign_in(self): 
        print('logged in')

# Sub Class/ Child Class/ Derived Class
'''
In this moc game, we want to ensure that every player type is "logged in" in order
to be able to play. To do so, we pass the parent class we want to inherit from, in 
this case it's the User class.
'''
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')

'''
Wizard and archer will have the inhereted sign_in functionality and the attack method. 
Each attack method is unique to their classes, however. They'll also have different 
properties
'''
wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()
print(isinstance(wizard1, Wizard)) #is wizard1 an instance of Wizard class?
print(isinstance(wizard1, Archer)) #is wizard1 an instance of Archer class?
print(isinstance(wizard1, User)) #is wizard1 an instance of User class?
print(isinstance(wizard1, object)) #is wizard1 an instance of object base class that python comes with? 
