# Private Vs Public Variables

class PlayerCharacter:
    def __init__(self, name, age):
        if age > 18:
            self._name = name #the use of underscore labels the variiable as "private"
            self._age = age

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old.')


player1 = PlayerCharacter('WinStone', 35)
player1.speak()