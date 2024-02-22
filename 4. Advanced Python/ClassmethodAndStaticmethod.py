# @classmethod and @staticmethod

class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod #decorator
    #first parameter for class method is cls, which stands for "class" (similar to how self is first param to class)
    def adding_things(cls, num1, num2): 
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    #in static methods, you do not have access to the cls
    def adding_things2(num1, num2): 
        return num1 + num2

#player1 = PlayerCharacter('Tom', 20)
player3 = PlayerCharacter.adding_things(2,3)

print(player3.age)