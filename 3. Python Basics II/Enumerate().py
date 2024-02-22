# Enumerate()

for i, char in enumerate('Helllooo'):
    print(i, char)

for i, char in enumerate([1, 2, 3]):
    print(i, char)

#loops through a list of 100 items
for i, char in enumerate(range(100)):
    print(i,char) #prints the index and value of the index
    if char == 50:
        print(f"index of 50 is: {i}") #prints the index of 50