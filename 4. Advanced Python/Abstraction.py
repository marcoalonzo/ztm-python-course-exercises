class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def run(self):
        print('run')

    def speak(self): #this speak method can now use name and age
        print(f'My name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('Winstone', 35)
#abstraction in action - Player1 has access to the speak method and can use it
player1.speak() 


