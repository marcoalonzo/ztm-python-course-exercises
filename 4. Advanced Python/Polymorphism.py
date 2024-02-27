# Polymorphism

# Parent Class
class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do nothing.')

    def attack(self):
        print('do nothing')


# Sub Class/ Child Class/ Derived Class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        #Since we accept User as our class parameter, we can then run user.attack within this class method
        User.attack(self) 
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: Arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)
print(wizard1.attack())
print(archer1.attack())

'''
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)
'''

#for char in [wizard1, archer1]
    #char.attack()