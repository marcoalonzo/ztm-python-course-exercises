class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
#1 Add nother Cat
#Answer:
class Garfield(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
'''Answer1:
my_cats = []
cat1 = Simon('Simon', 10)
cat2 = Sally('Sally', 2)
cat3 = Garfield('Garfield', 5)
my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)
'''
#Answer2 (Simplified):
my_cats = [Simon('Simon', 10), Sally('Sally', 2), Garfield('Garfield', 5)]

#3 Instantiate the Pet class with all your cats use variable my_pets
#Answer:
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
#Answer:
my_pets.walk()