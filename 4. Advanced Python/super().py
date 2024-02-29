#super()

# Parent Class
class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')
    

# Sub Class/ Child Class/ Derived Class
class Wizard(User):
    def __init__(self, name, power, email):
        #User.__init__(self,email)
        super().__init__(email) #super refers to the super class or the class above the subclass
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)
