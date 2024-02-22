# Range()

print(range(100))
print(range(0, 100))

#loops and prints out from 0-9
#(10 total numbers in the range)
for number in range(10): 
    print(number, end=' ')
print()

for _ in range(10):
    print('Hi', end=' ')
print()

#Step over is used to dictate an indicated skip
for number in range(0, 10, 2):
    print(number, end=' ')
print()

#step over in reverse can also be done
for number in range(0, 10, -1):
    print(number, end=' ')
print()

for number in range(10, 0, -1):
    print(number, end=' ')
print()

for number in range(10, 0):
    print(number, end=' ')
print()

for number in range(10, 0, -2):
    print(number, end=' ')
print()

'''
Loops twice. First it creates a range, an iterable object that has
10 items. Then converts that range into a list
'''
for _ in range(2):
    print(list(range(10)))