# Exercise Find Duplicates
# Check for duplicates in the list.
# Print the characters which have duplicates in the list.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#Answer (a):

new_list = []
dups = []

for value in some_list:
  if value not in new_list:
    new_list.append(value)
  else:
    dups.append(value)

print(dups)

#Answer (b):

duplicates = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)
