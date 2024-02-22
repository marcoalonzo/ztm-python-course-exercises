# Exercise Dictionary Methods

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 my copying the previous user and update the age value and username value.

#Answer:
user_profile = {
  'age': 34,
  'username': 'winstone',
  'weapons': ['gun', 'knife', 'shield', 'grenade'],
  'is_active': True,
  'clan': 'LVFC'
}

print(user_profile.keys())

user_profile['weapons'].append('rock')
print(user_profile)

user_profile.update({'is_active': False})
print(user_profile)

user_profile.update({'is_banned': False})
print(user_profile)

user_profile.update({'is_banned': True})
print(user_profile)

user_profile2 = user_profile.copy()
user_profile2.update({'age': 32})
user_profile2.update({'username': 'Luna'})
print(user_profile2)
