#Pure Functions
'''
The following function is considered pure since it will always provide the same
output and it does not create any side effects outside of it's own function
'''
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

