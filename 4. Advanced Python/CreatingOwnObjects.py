# OOP (Object-Oriented Programming)
class PlayerCharacter:
    membership = True #Class Object Attribute
    #__init__ method (constructor method) automatically called any time we instantiate
    def __init__(self, name = 'anonymous', age = 0): #self refers to the player character
        #if the player contains a membership, assign the attributes to self
        if (age >= 18): #game will error out if player is not > 18
            self.name = name #attribues/properties
            self.age = age
                
    def shout(self):
        print(f'My name is {self.name}')
    
player1 = PlayerCharacter('Tom', 19) #tom is over 18, so game will allow play
print(player1.shout())