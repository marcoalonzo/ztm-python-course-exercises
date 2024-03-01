# Multiple Inheritance

class User:
    def sign_in(self):
        print('logged in')


class Wizard(User): #Inherits from User
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User): #Inherits from User
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer): #HybridBorg inherits from Wizard and Arher
    def __init__(self, name, power, arrows): #this function will receive these parameters from the super classes
        #we call the archer init() and pass in the name and arrows in order to have access to these attributes
        Archer.__init__(self, name, arrows)
        #we call the wizard init() and pass in the name and power in order to have access to these attributes
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())


