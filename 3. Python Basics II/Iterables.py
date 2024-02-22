# Iterables

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item)

#iterates through the key:value pairs of the dict 'user'
for item in user.items():
    print(item)

#iterates through the keys of the dict 'user'
for item in user.keys():
    print(item)

#iterates through the values of the dict 'user'
for item in user.values():
    print(item)

'''
iterates through the key:value pairs of dict 'user'
and performs tuple unpacking (doesn't print as tuple)
'''
for item in user.items():
    key, value = item
    print(key, value)

'''
performs exact same action as the tuple unpacking above,
however, this is more readble and more commonly used method
'''
for key, value in user.items():
    print(key, value)