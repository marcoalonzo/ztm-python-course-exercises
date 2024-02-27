#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age 


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Mr. Whiskers', 3)
cat2 = Cat("Oliver", 1)
cat3 = Cat("Milo", 6)

# 2 Create a function that finds the oldest cat
def oldest(*ages):
    return max(ages)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old.")