class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    #def run(self):
    #    print('run')

    #def speak(self): #this speak method can now use name and age
    #    print(f'My name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('Winstone', 35)
#player1.speak()
print(player1.name)
print(player1.age)

player2 = {'name': 'winstone', 'age': 35}
print(player2['name'])
print(player2['age'])