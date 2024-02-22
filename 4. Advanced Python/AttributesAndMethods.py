# Attributes And Methods

class PlayerCharacter:
    # Class Object Attribute
    membership = True
    #__init__ methods (constructor method) automatically called any time we instantiate
    def __init__(self, name, age): #self refers to the player character
        if self.membership:     # Or PLayerCharacter.membership
            self.name = name #attributes/properties
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self, hello):
        print(f'{hello} {self.name}')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

player1.shout()
player2.shout()
player1.run('Hi')
player2.run('What up')
print(player1.membership, '\t', player1.name, '\t', player1.age)
print(player2.membership, '\t', player2.name, '\t', player2.age)