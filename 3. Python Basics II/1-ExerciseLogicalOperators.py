# Exercise Logical Operators

'''
Conditional Logic is all about writing code that makes sense, not only to you, but for other people reading your code. 
	• The idea is not to be extremely clever or really worry about short-circuiting
	• Minimal optimization is not worth losing readability over 
    • Code that is easy to understand is a sign of a good developer 
'''

is_magician = False
is_expert = True

# Check if magician and expert: "you are a master magician"
if is_magician and is_expert:
    print("You are a master magician")

# Check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("At least you\'re getting there.")

# Check if not a magician: "You need magic powers"
elif not is_magician:
    print("You need magic powers.")