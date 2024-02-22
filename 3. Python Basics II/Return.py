# Return

def sum1(num1, num2):
    return num1 + num2

'''
Invokes the function and returns the sum value, 
assigns it to the variable total
'''
total = sum1(10, 5)
'''
invokes the function sum again and returns the sum
value of 10 and the varlue of the variable "total".
Prints out the total (10 + 15)
'''
print(sum1(10, total))
#print()


def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    '''
    When we return this other function, we're using the parameters
    num1 and num2 that we called with sum(10,20)
    '''
    return another_func(num1, num2)
    '''
    the following two lines will never get executed becuase the return
    processed above automatically exists the function
    '''
    return 5
    print('hello')

total = sum2(10, 20)
print(total)