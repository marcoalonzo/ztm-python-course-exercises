#Error Handling

while True: #while loop is used to continue asking for an int, if one is not provided
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError: #if a value error exists, do the following:
        print('Please enter a number')
    '''
    A second value error will not output since the except block will only run once and
    as soon as it catches the error it's looking for, it will go back to the while loop
    '''
    except ValueError:
        print('!!!!!')
    except ZeroDivisionError: #if a 0 div error exists, do the following:
        print('Please enter age higher than 0')
    else: #if an integer is provided, print thanks and break the loop
        print('Thank you!')
        break



