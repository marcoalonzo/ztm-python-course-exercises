a = 'helloooooooooo'

#walrus syntax := assigns values to variables as part of a larger expression
if ((n := len(a)) > 10):
    print(f"too long {n} elements")

'''
While the length of 'a' is greater than 1, print the length of 'a', 
then reassign the value of 'a' to have one less elememt/letter
'''
while ((n := len(a)) > 1):
    print(n)
    #remove the last leter from variable 'a' everytime the loop runs
    a = a[:-1]

#prints the last remaining letter in variable 'a'
print(a)