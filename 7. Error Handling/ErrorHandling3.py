#Error Handling

while True:
    try:
        age = int(input('What is your age? '))
        10/age
        raise ValueError('hey cut it out')
    #except ValueError:
        #print('Please enter a number')
        #continue
    except ZeroDivisionError:
        print('Please enter age higher than 0')
        break
    else:
        print('Thank you!')
    finally: #runs at the end of everything, regarless
        print('ok, I am finally done')
    print('Can you hear me?') #this statement will only print when there are no break statement above

