# Functions

'''
This function is being defined by use and will print out the string
"hello" every time we call it
'''
def say_hello():
    print('Helllooooo!')

#this is calling the function we defined and will print out "hello"
say_hello()

'''
Display the image below where 0 is going to be ' ' and 1 is going to be *
'''
picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]
]

#function defined with loop code to iterate through the picture's rows and values
def show_tree():
    for array in picture:
        for item in array:
            if item:
                print('*', end='')
            else:
                print(' ', end='')
        print()


show_tree()
#print()
show_tree()
#print()
show_tree()
#print()
print(show_tree)