# Is vs ==

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print()

print(True == True)
print('1' == 1)
print([1, 2, 3] == [1, 2, 3])
print()

print(True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([1, 2, 3] is [1, 2, 3])
print()

print(True is True)
print('1' is '1')
'''
Everything time we create a list, it's added into memory. 
Everytime we create an additional list, it's going to be 
added into memery in a completely different location than 
the first list.
'''
print([] is [])
